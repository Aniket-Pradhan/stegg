from PIL import Image
from random import choice
from os.path import getsize
from binascii import b2a_hex

import cover_image

# constants
START_BUFFER = b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
END_BUFFER = b'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

class encoder:

    def check_steg(self):
        if self.max_secret_size <= 2 * self.secret_size:
            raise Exception("Secret size is too big for the cover image.")

    def read_secret(self, secret_path):
        self.max_secret_size = 3 * self.cover.num_pixels # Assuming an RGB image

        with open(secret_path, 'rb') as file:
            self.secret = file.read().strip()
        
        # adding buffers to isolate the message.
        self.secret = START_BUFFER + self.secret + END_BUFFER

        hex_text = b2a_hex(self.secret).decode('ascii')
        # convert hex to binary and fill the rest of the bitstream with random hex
        b = ''
        for ch in hex_text:
            tmp = bin(ord(ch))[2:]
            if len(tmp) < 7:
                for _ in range(0,(7-len(tmp))):
                    tmp = '0' + tmp
            b += tmp
        for _ in range(0,(self.max_secret_size - len(b)),7):
            b += str(bin(ord(choice('abcdef')))[2:])
        # final secret to be embedded
        self.secret = b
    
    def get_secret_size(self, secret_path):
        return 8 * getsize(secret_path) # in bits

    def __init__(self, cover_image_path, secret_path):
        # Cover image
        self.cover = cover_image.cover_image(cover_image_path)
        
        # the secret we want to embed. The secret is stored as plain text in one line.
        # We will open the file in binary format to read the file.
        # The length of plain text is the bytes of data we will have to hide.
        # For example, for a secret "Hello World" we will have to hide 11 bytes.
        self.read_secret(secret_path)
        self.secret_size = self.get_secret_size(secret_path)
        
        # check the number of pixels that can be modified. Ensure that the secret_message
        # can be embedded in the image
        self.check_steg()
    
    def encode(self):
        newIm = Image.new("RGB", (self.cover.image.size[0], self.cover.image.size[1]), "white")
        bitstream = iter(self.secret)
        for row in range(self.cover.image.size[1]):
            for col in range(self.cover.image.size[0]):
                # get the value for each byte of each pixel in the original image
                try:
                    red, green, blue = self.cover.image.getpixel((col,row))
                except:
                    print(self.cover.image.getpixel((col,row)))
                    exit()

                # get the new lsb value from the bitstream
                rb = next(bitstream)
                # modify the original byte with our new lsb
                red = self.set_lsb(red, rb)

                gb = next(bitstream)
                green = self.set_lsb(green, gb)

                bb = next(bitstream)
                blue = self.set_lsb(blue, bb)

                # add pixel with modified values to new image
                newIm.putpixel((col, row),(red, green, blue))

        newIm.save(str('steg_image.png'), 'png')
        print('created steg_image.png')        

    def set_lsb(self, in_byte, in_bit):
        b = list(bin(in_byte))
        b[-1] = in_bit
        return int(''.join(b),2)
