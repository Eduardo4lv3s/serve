from PIL import Image

imagem = Image.open("final.png")

bits = []
o = 0

for y in range(1250):
    for x in range(1250):
        if imagem.getpixel((x,y)) == (0,255,0):
            bits.append("1")
        elif imagem.getpixel((x,y)) == (0,0,255):
            bits.append("0")
        
byte = [[""]*1 for _ in range(194615)]
for w in range(len(bits)//8):
    for z in range(8):
        byte[w][0] += bits[z+w*8]

decodeit = open('hello_level.jpg', 'wb')

arquivo_bytes = [[]*1]
for bytes in range(194615):
    decodeit.write((int(byte[bytes][0],2)).to_bytes(1))
    
decodeit.close() 

print(arquivo_bytes)
    
