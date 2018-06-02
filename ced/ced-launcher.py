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

import argparse
import ced.lib.processing as processing

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program to decode email \
        protection from files/servers managed with Cloudflare.", epilog="It can \
         identify generally when you find the string '[email protected]'.")

    groupIO = parser.add_mutually_exclusive_group(required=True)
    groupIO.add_argument("-f", "--file", help="Input file to replace emails protected")
    groupIO.add_argument("-u", "--uri", help="URI to download and replace emails protected")

    groupInfo = parser.add_mutually_exclusive_group()
    groupInfo.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    processing.ced_main(args)
