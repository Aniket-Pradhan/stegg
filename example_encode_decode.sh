#!/bin/bash

# encode
echo "Encoding"
python scripts/main.py -e -c images/download.png -s temp_secret
echo "Encoded"

# decode
echo "Decoding"
python scripts/main.py -d -i steg_image.png
echo "Decoded"
