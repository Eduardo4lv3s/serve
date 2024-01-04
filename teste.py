import math

with open("imagem.jpg", "rb") as arqui_bytes:
    convertido_bit = []
    for x in arqui_bytes.read():
        convertido_bit.append(format(x, "0>8b"))

a = 0
r = round(math.sqrt(194615))

if r * r > 194615:
    a = 2
    
print(len(convertido_bit))
print()