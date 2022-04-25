#!/usr/bin/python3

from PIL import  Image, ImageDraw

my_image = Image.new("RGB", (800, 600), (0, 255, 0))
draw = ImageDraw.Draw(my_image)

for n in range(10):
    print(n)
    draw.rectangle((100 + n * 4, 200 + n * 4, 300, 400), fill=(0, 0, 255 - n * 10))

my_image.save("my_image.jpg", quality=95)
my_image.show()
