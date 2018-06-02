


# !/usr/bin/python3
# -*- coding: utf8 -*-
#
##################################################################################
#
#   This file is part of 'Cloudflare Email Decoder'.
#
#   Usufy is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import sys
import re
import requests
import logging


def request_file(uri):
    """
    Make a request and return its content
    
    Args:
        uri (string): The URI with the protected content
    
    Returns:
        object: Response object
    """
    r = requests.get(uri, stream=True, headers={"User-Agent": 'CED'})
    return r
    

def decode_email(encodedString):
    """
    Receive a string and process its value to make it readable

    Args:
        encodedString (string): The encoded email with CoudFlare CDN protection
    
    Returns:
        string: The decoded email
    """
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, 
        len(encodedString), 2)])
    return email


def replace_content(text, decode=False):
    """
    Check the links with regular expression to find encoded content 
    and replace it

    Args:
        text (string): Text to check
        decode (bool, optional): Set to decode content with utf-8 codification
    """
    emailregex = 'data-cfemail=\"([^\"]+)\"'
    tagregex = r'<a href="\/cdn-cgi\/l\/email-protection"[^>]*>([^<]+)<\/a>'
    for line in text:
        if decode:
            line = line.decode('utf-8')
        m = re.search(emailregex,line)
        if m:
            line = re.sub(tagregex, decode_email(m.group(1)), line)
        print(line)


def ced_main(args):
    """
    Main function called by launcher
    """
    logger = logging.getLogger('CED')	
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    logger.info("Starting ced-launcher.py ...")

    # With input file
    if args.file:
        logger.info("Trying to open the input file ...")

        try:
            lines = [line.rstrip('\n') for line in open(args.file)]
            replace_content(lines)
            logger.info("The replacements were done successfully")
        except Exception as e:
            sys.exit("ERROR: Ensure you have permission to read the input file.")

    # With URI
    elif args.uri:
        logger.info("Trying to get the content of the requested URI ...")

        try:
            replace_content(request_file(args.uri), True)
            logger.info("The replacements were done successfully")
        except Exception as e:
            sys.exit("ERROR: Ensure you have permission to write the output file.")