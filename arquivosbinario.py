import base64


with open("imagem_1.jpg", "rb") as image2string: 
    converted_string = base64.b64encode(image2string.read()) 
print (type(converted_string))

with open('encode.bin', "wb") as file: 
    file.write(converted_string)

  
  
file = open('encode.bin', 'rb') 
byte = file.read() 
file.close() 
  
decodeit = open('hello_level.jpeg', 'wb') 
decodeit.write(base64.b64decode((byte))) 
decodeit.close() 