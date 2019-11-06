import argparse
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

img_path = args["image"]

i = Image.open(img_path) 
pixels = i.load()
width, height = i.size

for y in range(height):
	for x in range(width):
		r=g=b=0
		if pixels[x, y][0]%2==1: r=0
		else: r=255
		if pixels[x, y][1]%2==1: g=0
		else: g=255
		if pixels[x, y][2]%2==1: b=0
		else: b=255
		pixels[x, y] = (r, g, b)

i.show()
