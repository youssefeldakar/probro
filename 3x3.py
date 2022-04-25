from PIL import  Image, ImageDraw

my_image = Image.new("RGB" , (800, 600) , (0, 255, 0))
draw = ImageDraw.Draw(my_image)

draw.rectangle((  0,   0, 200-1, 200-1), fill=(  0,   0, 255))
draw.rectangle((200,   0, 400-1, 200-1), fill=(255,   0,   0))
draw.rectangle((400,   0, 600-1, 200-1), fill=(  0, 255, 255))

draw.rectangle((  0, 200, 200-1, 400-1), fill=(255,   0, 255))
draw.rectangle((200, 200, 400-1, 400-1), fill=(255,   0,   0))
draw.rectangle((400, 200, 600-1, 400-1), fill=(  0, 255, 255))

draw.rectangle((  0, 400, 200-1, 600-1), fill=(255,   0,   0))
draw.rectangle((200, 400, 400-1, 600-1), fill=(255,   0, 255))
draw.rectangle((400, 400, 600-1, 600-1), fill=(255, 255,   0))

my_image.save("my_image.jpg", quality=95)
my_image.show()
