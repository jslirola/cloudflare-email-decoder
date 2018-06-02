# CloudFlare Email Decoder

Program to decode email protection from files/servers managed with Cloudflare. It can identify generally when you find the string `[email protected]`.

## Installation

```bash
git git@github.com:jslirola/cloudflare-email-decoder.git
cd cloudflare-email-decoder
sudo python3 setup.py install
```

## Usage

```bash
python3 ced-launcher.py -h
```

It will show help to run the script

```bash
usage: ced-launcher.py [-h] (-f FILE | -u URI) [-v]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file to replace emails protected
  -u URI, --uri URI     URI to download and replace emails protected
```

Basic examples:

```bash
python3 ced/ced-launcher.py -f tmp/encoded_content.txt
[...]

python3 ced/ced-launcher.py -u "http://example"
[...]
INFO:CED:The replacements were done successfully

python3 ced/ced-launcher.py -f tmp/encoded_content.txt > /tmp/decoded.txt
[...]
```

### Collaborators

- Félix Brezo [@febrezo](https://github.com/febrezo/)