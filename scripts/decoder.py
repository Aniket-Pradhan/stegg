from PIL import Image
from binascii import a2b_hex

# constants
START_BUFFER = b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
END_BUFFER = b'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

class decoder:

    def extract_message(self, message):
        start_buffer_index = message.find(START_BUFFER)
        end_buffer_index = message.find(END_BUFFER)

        if start_buffer_index == -1 or end_buffer_index == -1:
            raise Exception("Could not find either of the buffers")

        return message[start_buffer_index+len(START_BUFFER):end_buffer_index].decode("utf-8") 

    def parse_binary(self, message_binary):
        byte_arr = []
        for i in range(0, len(message_binary), 7):
            byte_arr.append(message_binary[i:i+7])
        
        c = ''
        for i in byte_arr:
            c += chr(int(i,2))
        if len(c) % 2 != 0:
            c += 'A'
        return a2b_hex(c[:-10].encode('ascii'))

    def decode(self):
        message_binary = ""
        for row in range(self.steg_image.size[1]):
            for col in range(self.steg_image.size[0]):
                red, green, blue = self.steg_image.getpixel((col,row))
                
                message_binary += bin(red)[-1]
                message_binary += bin(green)[-1]
                message_binary += bin(blue)[-1]

        message = self.parse_binary(message_binary)
        message = self.extract_message(message)
        print(message)
        return message

    def __init__(self, steg_image_path):
        self.steg_image = Image.open(steg_image_path)