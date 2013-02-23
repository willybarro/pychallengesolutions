# http://www.pythonchallenge.com/pc/def/peak.html

import pickle

def main():
	with open("5.p", "rb") as f1:
		o = pickle.load(f1)

	with open("5.out", "w") as f2:
		for a in o:
			line = ""
			for s in a:
				line += s[0] * s[1]
			line += "\n"
			f2.write(line)

main()

'''
- A dica fornecida foi "peak hole", e ele pede pra pronunciar isso em voz alta.
- A pronuncia fica parecida com "pickle", que é um módulo de serialização nativo do python.

- No código fonte da página, existe o elemento "<peakhell src="banner.p"/>"
	- Este arquivo é um objeto python serializado.

- Ao carregar o arquivo, um objeto com tuplas no formato (simbolo, numero) é encontrado.
	- Os simbolos são sempre " " e "#", e os numeros parecem ser quantidades. Logo, pode ser uma Ascii art.

- Ao mandar imprimir em arquivo os simbolos repetidos o numero de vezes da tupla, aparece a palavra "channel"

Logo, o novo desafio é o http://www.pythonchallenge.com/pc/def/channel.html
'''