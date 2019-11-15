import sys
import cv2

def comps(file1, file2):
	im1 = cv2.imread(file1)
	im2 = cv2.imread(file2)

	psnr = cv2.PSNR(im1,im2)
	return psnr

file1 = sys.argv[1]
file2 = sys.argv[2]

psnr = comps(file1, file2)
print(psnr)

