# stegg

## Setup

First create and activate a virtual environment (optional)

```bash
python -m virtualenv ./.venv
source ./.venv/bin/activate
```

Now, install the dependencies.

```bash
pip install -r requirements.txt
```

Now you are ready to go. Follow the instructions ahead. :D

### How to encode and decode messages into images

The `main.py` in `encoder_decoder/` provides an easy framework using which text messages can be encoded and decoded.

```bash
$ python encoder_decoder/main.py -h
-h, --help            show this help message and exit
-c COVER, --cover COVER
                     Path to the cover image
-s SECRET, --secret SECRET
                     Path to the secret/payload.
-e, --encode          Use this arg to encode the secret
-i IMAGE, --image IMAGE
                     Path to image to decode
-d, --decode          Use this arg to encode the secret

```

This help menu summarizes the operations of the file. Currently only RGB images, and plain-text secret messages are supported.

An example script: `example_encode_decode.sh` is provided in the root of the repo which can be used to create a sample stego-image from the secret present.

### Histogram-attack steganlysis

You can use `main.py` in `histogram_attack/` to check whether a suspicious image has been encoded using LSB steganography. You would require the cover image alongside it as well.

```bash
$ python histogram_attack/main.py -h
usage: main.py [-h] -c COVER -s SUSPICIOUS

optional arguments:
 -h, --help            show this help message and exit
 -c COVER, --cover COVER
                       Path to the cover image
 -s SUSPICIOUS, --suspicious SUSPICIOUS
                       Path to the suspicious image.
```

You can use these arguments to specify the locations of the cover and suspicious images and get the result as well. An example script: `example_hist_attack.sh` is also provided in the root of the project to see a demo (please run `example_encode_decode.sh` before running this script.).
