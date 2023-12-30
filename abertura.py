from PIL import Image

image = Image.open("imagem_1.jpg")
print(image.getpixel((10,10)))
image.show()
