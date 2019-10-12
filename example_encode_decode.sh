#!/bin/bash

# encode
echo "Encoding"
python encoder_decoder/main.py -e -c images/download.png -s temp_secret
echo "Encoded"

# decode
echo "Decoding"
python encoder_decoder/main.py -d -i steg_image.png
echo "Decoded"
