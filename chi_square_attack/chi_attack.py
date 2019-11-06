import numpy
import argparse
from PIL import Image
from scipy import stats

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

imagepath = args["image"]

i = Image.open(imagepath) 
pixels = i.load()
width, height = i.size
chunk=5124
last_pval=0

chis = []
pvals = []

# num_iter = 0

# for sz in range(chunk, height*width, chunk):
# 	num_iter += 1

# print(num_iter)
# exit()

chunk = height*width-1

for sz in range(chunk, height*width, chunk):
	histogram = [0]*256
	for y in range(height):
		if y*height>sz:
			break
		for x in range(width):
			if type(pixels[x,y]) is tuple:
				for k in range(len(pixels[x, y])):
					cur_pixel = pixels[x, y][k]
					histogram[cur_pixel]+=1
			else:
				cur_pixel = pixels[x, y]
				histogram[cur_pixel]+=1
	obs = []
	exp = []
	X=0
	for y in range(1, len(histogram), 2):
		x=histogram[y-1]
		z=(histogram[y-1]+histogram[y])/2
		if x>0 and z>0:
			obs.append(x)
			exp.append(z)
	obs = numpy.array(obs)
	exp = numpy.array(exp)	
	
	chi,pval = stats.chisquare(obs, exp)
	
	chis.append(chi)
	pvals.append(pval)
	# print(pval)
	# if pval<=0.01:
	# 	if last_pval < 0.01:
	# 		print("Cover")
	# 		exit()
	# 	else:
	# 		break
	# last_pval=pval

# print(sum(pvals), sum(chis))
# print("Stego, length: %d" % sz)
if abs(sum(pvals) - 0.1) <= 0.1:
	print("Image is not encoded with a secret message")
else:
	print("Steg-Image")
