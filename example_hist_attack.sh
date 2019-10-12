#!/bin/bash

echo "Please run example_encode_decode.sh before running this example script"
echo ""

echo "Testing 'images/download.png' and 'steg_image.png' for steganography"
echo "python histogram_attack/main.py -c images/download.png -s steg_image.png"
echo ""
python histogram_attack/main.py -c images/download.png -s steg_image.png
echo ""

echo "Testing un-stegged images, i.e. 'images/download.png' and 'images/download.png'"
echo "python histogram_attack/main.py -c images/download.png -s images/download.png"
echo ""
python histogram_attack/main.py -c images/download.png -s images/download.png
echo ""
