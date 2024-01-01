from PIL import Image

with open("imagem_1.jpg", "rb") as arqui_bytes:
    convertido_bytes = arqui_bytes.read()


imagem = Image.new("RGB", (1250,1250),(255,255,255))

convertido_bit = []

for x in convertido_bytes:
    convertido_bit.append(format(x, "0>8b"))


v = 0
w = 0

x2 = 0
y2 = 0

for y in range(441):
        for x in range(442):
            for z in range(8):
                if v < 1556920:
                    if x2 < 1250:
                        if convertido_bit[w][z] == "1":
                            imagem.putpixel((x2, y2), (0,255,0))
                        if convertido_bit[w][z] == "0":
                            imagem.putpixel((x2, y2), (0,0,255))
                        x2+=1
                    else:
                        x2 = 0
                        y2+=1
                    
                v+=1
            w+=1



imagem.show()
imagem.save('final.png', "png")
