import argparse
import skimage
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from hist_attack import histogram_attack

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cover", required=True, help="Path to the cover image")
ap.add_argument("-s", "--suspicious", required=True, help="Path to the suspicious image.")
ap.add_argument("-n", "--noise", required=False, help="Add some noise to the image and then check.", action="store_true")

args = vars(ap.parse_args())

if __name__ == "__main__":
    cover_image_path = args["cover"]
    suspicious_image_path = args["suspicious"]
    add_noise = args["noise"]

    if add_noise:
        img = skimage.io.imread(cover_image_path)/255.0
        gimg = skimage.util.random_noise(img, mode="gaussian")
        im2 = Image.fromarray((gimg*255).astype(np.uint8))

        cover_image_path = cover_image_path.strip().split("/")
        img_name = cover_image_path.pop(len(cover_image_path) - 1)
        cover_image_path.append("noisy_image_" + str(img_name))
        img_name = ""
        for i in cover_image_path:
            img_name += str(i) + "/"
        cover_image_path = img_name[:len(img_name)-1]
        im2.save(cover_image_path)

    hist_attack = histogram_attack(cover_image_path, suspicious_image_path)
    hist_attack.attack()
    is_stego = hist_attack.analyze()

    if is_stego:
        print("The picture is encoded using LSB steganography!")
    else:
        print("The picture is clean")
