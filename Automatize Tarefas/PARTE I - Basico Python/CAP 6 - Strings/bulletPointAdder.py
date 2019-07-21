#! python3
# bulletPointAdder.py – Acrescenta marcadores da Wikipedia no início
# de cada linha de texto do clipboard.

import pyperclip
text = pyperclip.paste()
# TODO: Separa as linhas e acrescenta asteriscos.

# Separa as linhas e acrescenta os asteriscos.
lines = text.split('\n')
for i in range(len(lines)): # percorre todos os índices da lista "lines" em um loop
	lines[i] = '* ' + lines[i] # acrescenta um asterisco em cada string da lista "lines"

text = '\n'.join(lines)
pyperclip.copy(text)

''' 
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
e depois executar o programa bulletPointAdder.py, o clipboard conterá o
seguinte:
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
'''