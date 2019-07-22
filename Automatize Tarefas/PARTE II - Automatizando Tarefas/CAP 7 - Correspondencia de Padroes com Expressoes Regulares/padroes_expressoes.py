'''
Talvez você já esteja acostumado a pesquisar um texto
pressionando CTRL-F e digitando as palavras que estiver
procurando. As EXPRESSÕES REGULARES vão um passo além: elas
permitem especificar um padrão de texto a ser procurado. Talvez
você não saiba exatamente o número de um telefone comercial,
porém, se morar nos Estados Unidos ou no Canadá, saberá que ele
contém três dígitos seguidos de um hífen e depois mais quatro
dígitos.
'''

# Encontrando padrões de texto sem usar expressões regulares

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True
	
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242')) # True
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))  # False

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: ' + chunk)
print('Done')
''' Output:
Phone number found: 415-555-1011
Phone number found: 415-555-9999
Done
'''

# Encontrando padrões de texto com expressões regulares
'''
As expressões regulares (regular expressions), chamadas de regexes por
questões de concisão, correspondem a descrições para um padrão de texto.
Por exemplo, um \d é uma regex que representa um dígito – ou seja, qualquer
numeral único entre 0 e 9. A regex \d\d\d-\d\d\d-\d\d\d\d é usada pelo Python
para fazer a correspondência do mesmo texto conforme feito pela função
isPhoneNumber(): uma string com três números, um hífen, mais três números,
outro hífen e quatro números. Qualquer outra string não corresponderá à
regex \d\d\d-\d\d\d-\d\d\d\d.
'''

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# r - raw string -> string pura 
# Digitar r'\d\d\d-\d\d\d-\d\d\d\d' é mais fácil do que '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group()) # Phone number found: 415-555-4242

# Mais correspondência de padrões com expressões regulares
'''
Suponha que você queira separar o código de área do restante do número de
telefone. A adição de parênteses criará grupos na regex: (\d\d\d)-(\d\d\d-
\d\d\d\d). Então você poderá usar o método group() do objeto de
correspondência para obter o texto correspondente de apenas um grupo.
'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1) # '415'
mo.group(2) # '555-4242'
mo.group(0) # '415-555-4242'
mo.group()  # '415-555-4242'

mo.groups() # ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)   # 415
print(mainNumber) # 555-4242

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1) # '(415)'
mo.group(2) # '555-4242'

# Fazendo a correspondência de vários grupos com pipe
'''
O caractere | é chamado de pipe. Podemos usá-lo em qualquer lugar em que
quisermos fazer a correspondência de uma entre várias expressões. Por
exemplo, a expressão regular r'Batman|Tina Fey' corresponde a 'Batman' ou a
'Tina Fey'.
''' 

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group() # 'Batman'
mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group() # 'Tina Fey'

'''
Podemos encontrar todas as ocorrências correspondentes com o método
findall() que será discutido na seção “Método findall()”.
'''

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()  # 'Batmobile'
mo.group(1) # 'mobile'

# Correspondência opcional usando ponto de interrogação
'''
Às vezes, há um padrão ao qual você quer corresponder somente de forma
opcional. Isso quer dizer que a regex deve encontrar uma correspondência
independentemente de essa porção de texto estar ou não presente.
'''
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group() # 'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group() # 'Batwoman'

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group() # '415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group() # '555-4242'

# Correspondendo a zero ou mais ocorrências usando asterisco
''''
O * (chamado de asterisco) quer dizer “corresponda a zero ou mais” – o
grupo que antecede o asterisco pode ocorrer qualquer número de vezes no
texto. Esse grupo poderá estar totalmente ausente ou ser repetido diversas
vezes. Vamos dar uma olhada no exemplo contendo Batman novamente.
'''
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group() # 'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group() # 'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group() # 'Batwowowowoman'














