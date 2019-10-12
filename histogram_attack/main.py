import argparse

from hist_attack import histogram_attack

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cover", required=True, help="Path to the cover image")
ap.add_argument("-s", "--suspicious", required=True, help="Path to the suspicious image.")

args = vars(ap.parse_args())

if __name__ == "__main__":
    cover_image_path = args["cover"]
    suspicious_image_path = args["suspicious"]

    hist_attack = histogram_attack(cover_image_path, suspicious_image_path)
    hist_attack.attack()
    is_stego = hist_attack.analyze()

    if is_stego:
        print("The picture is encoded using LSB steganography!")
    else:
        print("The picture is clean")
