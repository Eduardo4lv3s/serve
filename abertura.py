from PIL import Image

image = Image.open("nova.png")
print(image.getpixel((10,10)))
image.show()
