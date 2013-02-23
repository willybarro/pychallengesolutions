# http://www.pythonchallenge.com/pc/def/map.html

originalString = "http://www.pythonchallenge.com/pc/def/map.html"
map = str.maketrans("klmnopqrstuvwxyzabcdefghij", "mnopqrstuvwxyzabcdefghijkl")
print(originalString.translate(map))

'''
O texto de retorno é:
i hope you didnt translate it by hand. thats what computers are for. doing it in
by hand is inefficient and that's why this text is so long. using string.maketr
ans() is recommended. now apply on the url.


Ele pede pra aplicar na url, logo, aplicando no map.html vira ocr.jvon.
Arquivos .jvon não existem, logo, ocr.html
'''