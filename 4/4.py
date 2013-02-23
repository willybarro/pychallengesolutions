# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request
import re

def main():
	nothing = "63579"
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

	for n in range(262):
		requestUrl = url % nothing
		response = urllib.request.urlopen(requestUrl)
		responseString = response.read().decode('utf-8')

		m = re.search("(?:next nothing is )([0-9]+)", responseString)
		nothing = m.group(1)
		print(n, nothing)

		if(n == 262):
			print(responseString)

main()


'''
Passos:

Ao chegar no nothing = 16044, apareceu uma tela escrito: Yes. Divide by two and keep going.
Logo, divindo fica 8022


Ao chegar no nothing = 82683 da segunda iteracao, recebi a mensagem: You've been misleaded to here. Go to previous one and check.
O numero anterior foi o 82682.
Nessa tela, existe uma dica, dizendo que devo procurar apenas por "next nothing is"

Ao chegar no nothing = 66831 apareceu uma mensagem escrita "peak.html", que é a próxima fase.
'''