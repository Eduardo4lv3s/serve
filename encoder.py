from PIL import Image
import math

with open("imagem.jpg", "rb") as arqui_bytes:
    convertido_bit = []
    for x in arqui_bytes.read():
        convertido_bit.append(format(x, "0>8b"))

tamanho_arquivo = len(convertido_bit)
tamanho_bits = 1556920

def calcula_raiz(numero):
    r = round(math.sqrt(numero))
    if r * r < numero:
        r += 1
    return r

v = 0
w = 0

x2 = 0
y2 = 0

imagem = Image.new("RGB", 
                   (calcula_raiz(tamanho_arquivo*8),calcula_raiz(tamanho_arquivo*8)),
                   (255,255,255))

for y in range(calcula_raiz(tamanho_arquivo)):
        for x in range(calcula_raiz(tamanho_arquivo)):
            for z in range(8):
                if v < len(convertido_bit)*8:
                    if x2 >= calcula_raiz(tamanho_arquivo*8):
                        x2 = 0
                        y2+=1
                    if convertido_bit[w][z] == "1":
                        imagem.putpixel((x2, y2), (0,255,0))
                    if convertido_bit[w][z] == "0":
                        imagem.putpixel((x2, y2), (0,0,255))
                    x2+=1     
                v+=1
            w+=1



imagem.save('final.png', "png")
imagem.show()