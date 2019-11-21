import argparse
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-b", "--bit", required=False, default=0, help="Path to the image")
args = vars(ap.parse_args())

img_path = args["image"]
bit = int(args["bit"])

i = Image.open(img_path) 
pixels = i.load()
width, height = i.size

for y in range(height):
	for x in range(width):
		r = g = b = 0

		red_pix = pixels[x, y][0] >> bit
		green_pix = pixels[x, y][1] >> bit
		blue_pix = pixels[x, y][2] >> bit

		if red_pix % 2 == 1:
			r = 255
		else:
			r = 0
		if green_pix % 2 == 1:
			g = 255
		else:
			g = 0
		if blue_pix % 2 == 1:
			b = 255
		else:
			b = 0
		pixels[x, y] = (r, g, b)

i.show()
