import argparse

from encoder import encoder
from decoder import decoder

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cover", required=False, help="Path to the cover image")
ap.add_argument("-s", "--secret", required=False, help="Path to the secret/payload.")
ap.add_argument("-e", "--encode", required=False, help="Use this arg to encode the secret", action="store_true")
ap.add_argument("-i", "--image", required=False, help="Path to image to decode")
ap.add_argument("-d", "--decode", required=False, help="Use this arg to encode the secret", action="store_true")

args = vars(ap.parse_args())

if __name__ == "__main__":
    encode = args["encode"]
    decode = args["decode"]
    if encode == decode:
        print("Invalid use of arguments.")
        exit()
    
    if encode:
        assert args.get("cover") != None
        assert args.get("secret") != None

        cover_image_path = args["cover"]
        secret_path = args["secret"]

        steg_encoder = encoder(cover_image_path, secret_path)
        steg_encoder.encode()
    
    if decode:
        assert args.get("image") != None
        image_path = args["image"]
        steg_decoder = decoder(image_path)
        steg_decoder.decode()
