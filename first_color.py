#!/usr/bin/python3

from PIL import Image, ImageDraw

my_image = Image.new("RGB", (800, 600), (0, 55, 0))
draw = ImageDraw.Draw(my_image)

draw.rectangle((100,   0, 400, 300), fill=(  0, 128,   0), outline=(0, 128, 0))
draw.rectangle((100, 200, 300, 400), fill=(  0,   0, 255))
my_image.save("my_image.jpg", quality=95)
my_image.show()
