# stegg

## How to encode and decode messages into images?

The `main.py` provides an easy framework using which text messages can be encoded and decoded.

```python
$ python main.py -h

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

An example script is provided in the root of the repo which can be used to create a sample stego-image from the secret present.
