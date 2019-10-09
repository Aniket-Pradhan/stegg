from PIL import Image

class cover_image:

    def __init__(self, cover_image_path):
        self.image = Image.open(cover_image_path)
        self.image_type = cover_image_path.split('.')[-1]
        # number of pixels that can be manipulated
        self.num_pixels = self.image.size[1] * self.image.size[0]
