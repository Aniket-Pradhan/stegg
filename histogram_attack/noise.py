import skimage
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img_path="E:/DIP/project/stegg/images/download.png"
img = skimage.io.imread(img_path)/255.0
gimg = skimage.util.random_noise(img, mode="gaussian")
im2 = Image.fromarray((gimg*255).astype(np.uint8))
im2.save("image2.png")