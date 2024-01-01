import base64
from PIL import Image

def codifica_para_imagem(nome_arquivo):
    with open(nome_arquivo, "rb") as image_string: 
        converted_string = base64.b64encode(image_string.read()) 

    #print(converted_string)
    imagem = Image.new("RGB", (4200,4000),(255,255,255))

    altura = len(converted_string)*8//1000+1
    largura = 1000

    arquivo_bit = []
    for i in range(len(converted_string)):
        arquivo_bit += format(converted_string[i], "0>8b") 
    print(len(arquivo_bit))
    
    
    for y in range(2153):
        for x in range(2000):
            if y+x < 16607232:
                if arquivo_bit[y+x] == '1':
                    
                    imagem.putpixel((10, 10), (255,0,0))
                    
                elif arquivo_bit[y+x] == '0':
                    imagem.putpixel((x, y), (0, 255, 0))
                    
    

    imagem.save('nova.png', "png")
    imagem.show()
codifica_para_imagem("imagem_1.jpg")

def decodifica_para_arquivo(nome_imagem):
    imagem = Image.open(nome_imagem)
    bit = []
    
    for y in range(1780):
        for x in range(1000):
            if imagem.getpixel((x,y)) == (255,0,0):
                bit += '1'
            elif imagem.getpixel((x,y)) == (0, 255, 0):
                bit += '0'

    
    print(len(bit))
    

    

#decodifica_para_arquivo("nova.png")