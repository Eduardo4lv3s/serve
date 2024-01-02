with open("imagem_1.jpg", "rb") as arqui_bytes:
    convertido_bytes = arqui_bytes.read()

a = 2

print(convertido_bytes)
#print((255).to_bytes(a))