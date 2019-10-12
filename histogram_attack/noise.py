import skimage
import matplotlib.pyplot as plt
img_path="E:/DIP/project/stegg/images/download.png"
img = skimage.io.imread(img_path)/255.0
gimg = skimage.util.random_noise(img, mode="gaussian")
plt.imsave('test.png', gimg)