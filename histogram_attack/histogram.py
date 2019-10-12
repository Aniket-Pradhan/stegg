from PIL import Image
import numpy as np

class histogram:

    def _compute_histogram(self, image):
        image = np.array(image)
        _image = image.flatten().tolist()
        
        _hist = np.zeros(256)
        for i in range(len(_hist)):
            _hist[i] = int(_image.count(i))
        
        hist = []
        for i in range(len(_hist)):
            hist.append(int(_hist[i]))
        
        return hist

    def compute_histogram(self):
        r_hist = self._compute_histogram(self.r_image)
        g_hist = self._compute_histogram(self.g_image)
        b_hist = self._compute_histogram(self.b_image)

        return [r_hist, g_hist, b_hist]

    def __init__(self, in_image):
        self.image = in_image # of type Image
        self.r_image, self.g_image, self.b_image = self.image.split() # get different rgb channels
