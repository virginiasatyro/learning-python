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