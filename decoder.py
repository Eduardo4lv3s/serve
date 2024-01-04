from PIL import Image

imagem = Image.open("final.png")

bits = []
o = 0

for y in range(1248):
    for x in range(1248):
        if imagem.getpixel((x,y)) == (0,255,0):
            bits.append("1")
        elif imagem.getpixel((x,y)) == (0,0,255):
            bits.append("0")
        
byte = [[""]*1 for _ in range(194615)]
for w in range(len(bits)//8):
    for z in range(8):
        byte[w][0] += bits[z+w*8]

with open("imagem_convertida.jpg", "wb") as decodifica:
    for bytes in range(194615):
        decodifica.write((int(byte[bytes][0],2)).to_bytes(1, "big"))
