'''
Suponha que você tenha um valor de lista como:
spam = ['apples', 'bananas', 'tofu', 'cats']
Crie uma função que aceite um valor de lista como argumento e retorne uma
string com todos os itens separados por uma vírgula e um espaço, com and
inserido antes do último item. Por exemplo, se passarmos a lista spam anterior
à função, 'apples, bananas, tofu, and cats' será retornado. Porém sua função
deverá ser capaz de trabalhar com qualquer valor de lista que ela receber.
'''

def virgulas(lista):
	string_aux = ''
	for i in range(len(lista)):
		if i == (len(lista) - 1):
			string_aux = string_aux + lista[i]
		elif i == (len(lista) - 2):
			string_aux = string_aux + lista[i] + ' and '
		else:
			string_aux = string_aux + lista[i] + ', '
	return string_aux
		
spam = ['apples', 'bananas', 'tofu', 'cats']
print(virgulas(spam))