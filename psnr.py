import cv2

def comps(name1,name2):
	im1 = cv2.imread(name1)
	im2 = cv2.imread(name2)

	psnr = cv2.psnr(im1,im2)
	return (psnr)

#name1 and name2 are file name of images
#for that directory for computing PSNR
#anikhet please use your args function to do the magic

out = comps(name1,name2)
print(out)

