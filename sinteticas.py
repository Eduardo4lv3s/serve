from PIL import Image
import os

IMPUT_FOLDER = "imput"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(IMPUT_FOLDER, filename)

def triangle(size):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    imagem = Image.new("RGB", (size, size), WHITE)

    for x in range(size):
        for y in range(size):
            if x < y:
                imagem.putpixel((x, y), BLACK)
    return imagem

def bandeira_franca(height):
    width = 3*height//2
    BLUE = (0, 85, 164)
    WHITE = (255, 255, 255)
    RED = (239, 65, 53)
    imagem = Image.new("RGB", (width, height), WHITE)

    offset = width//3
    for x in range(offset):
        for y in range(height):
            imagem.putpixel((x, y), BLUE)
            imagem.putpixel((x + 2*offset, y), RED)
    return imagem

def bandeira_japao(height):
    width = 3*height//2
    WHITE = (255, 255, 255)
    RED = (173, 35, 51)
    
    r = 3*height//10
    c = (width//2, height//2)
    imagem = Image.new("RGB", (width, height), WHITE)
    for x in range(c[0]-r, c[0]+r):
        for y in range(c[1]-r, c[1]+r):
            if (x-c[0])**2 + (y-c[1])**2 <= r**2:
                imagem.putpixel((x, y), RED)

    return imagem

if __name__ == "__main__":
    bandeira = bandeira_japao(700)
    bandeira.show()
