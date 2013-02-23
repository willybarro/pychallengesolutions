# http://www.pythonchallenge.com/pc/def/channel.zip

import pickle
import zipfile
import re

def main():
	writeOut()

def writeOut():
	nothing = "90052"
	with open("6.out", "w") as fout:
		with zipfile.ZipFile("6_channel.zip", "r") as z:
			while(nothing != ""):
				filename = nothing + ".txt"
				f = z.open(filename)
				comment = z.getinfo(filename).comment.decode('utf-8')
				content = f.readline().decode('utf-8')

				fout.write(comment)

				m = re.search("(?:[Nn]ext nothing is )([0-9]+)", content)
				if m != None:
					nothing = m.group(1)
				else:
					nothing = ""

main()


'''
Existia uma dica no código dizendo "<-- zip -->"
- Existe um método chamado zip no python
	- Não é isso

- Ao alterar a url para channel.zip, consegui baixar um arquivo zipado, cheio de arquivos.
No readme, diz para eu começar com o arquivo 90052.
- Dentro dele, temos de novo o "next nothing is", que eu vi no 4o desafio.

- Depois de terminar de iterar por todos os arquivos, apareceu a mensagem "collect the comments".
Deve ter algo a ver com os comentarios de cada arquivo no zip.

- Refiz o loop, agora salvando os comentarios em um arquivo de saída.

- Apareceu em Ascii art a palavra "hockey", ao tentar entrar em hockey.html. Apareceu: "it's in the air. look at the letters."

- Olhando para o Ascii art, cada uma das letras grandes é formada por várias letras normais, que formam a palavra "oxygen".
	Agora o it's in the air faz sentido

Novo desafio: http://www.pythonchallenge.com/pc/def/oxygen.html

'''