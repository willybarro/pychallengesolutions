# http://www.pythonchallenge.com/pc/def/equality.html

import re

def main():
	fstring = open("3.in", "r").read()

	# procura todas as letras pequenas com 3 guardas grandes em volta
	m = re.findall("[^A-Z]([A-Z]{3}[a-z][A-Z]{3})[^A-Z]", fstring)
	
	# pega só as letras pequenas do que sobrou
	saida = ""
	for c in m:
		m2 = re.search("[a-z]", c)
		saida += m2.group(0)

	print(saida)

main()