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
# http://www.regular-expressions.info/
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

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group() # 'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group() # 'Batwowowowoman'
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None # True

# Correspondendo a repetições específicas usando chaves
'''
(Ha){3}
(Ha)(Ha)(Ha)

(Ha){3,5}
((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
'''
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group() # 'HaHaHa'
mo2 = haRegex.search('Ha')
mo2 == None # True

#Correspondências greedy e nongreedy
'''
As expressões regulares em Python são greedy (gulosas) por default, o que
significa que, em situações ambíguas, a correspondência será feita com a
maior string possível. Na versão nongreedy (não gulosa) das chaves, que faz a
correspondência com a menor string possível, um ponto de interrogação é
usado depois da chave de fechamento.
'''
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group() # 'HaHaHaHaHa'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group() # 'HaHaHa'

# Método findall()
'''
Além do método search(), os objetos Regex também têm um método findall().
Enquanto search() retorna um objeto Match do primeiro texto correspondente
na string pesquisada, o método findall() retorna as strings de todas as
correspondências na string pesquisada.
'''

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group() # '415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # não tem nenhum grupo
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # ['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # tem grupos
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # [('415', '555', '9999'), ('212', '555', '0000')]

# Classes de caracteres
'''
Classe de caract. abreviada     Representa
\d                              Qualquer dígito de 0 a 9.
\D                              Qualquer caractere que não seja um dígito de 0 a 9.
\w                              Qualquer letra, dígito ou o caractere underscore. (Pense nisso como uma correspondência decaracteres de “palavra”.)
\W                              Qualquer caractere que não seja uma letra, um dígito ou o caractere underscore.
\s                              Qualquer espaço, tabulação ou caractere de quebra de linha. (Pense nisso como uma correspondência de caracteres de “espaço”.)
\S                              Qualquer caractere que não seja um espaço, uma tabulação ou uma quebra de linha.
'''

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# Criando suas próprias classes de caracteres

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
# ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

# Acento circunflexo e o sinal de dólar
'''
O símbolo de acento circunflexo (^) também pode ser usado no início de uma
regex para indicar que uma correspondência deve ocorrer no início de um
texto pesquisado. Da mesma maneira, podemos colocar um sinal de dólar ($)
no final da regex para indicar que a string deve terminar com esse padrão de
regex.
'''

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
# <_sre.SRE_Match object; span=(0, 5), match='Hello'>
beginsWithHello.search('He said hello.') == None # True

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
# <_sre.SRE_Match object; span=(16, 17), match='2'>
endsWithNumber.search('Your number is forty two.') == None # True

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
# <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None # True
wholeStringIsNum.search('12 34567890') == None   # True

# Caractere-curinga
'''
O caractere . (ou ponto) em uma expressão regular é chamado de caracterecuringa
e corresponde a qualquer caractere, exceto uma quebra de linha. Por
exemplo, digite o seguinte no shell interativo:
'''
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']

# Correspondendo a tudo usando ponto-asterisco
'''
Às vezes, vamos querer fazer uma correspondência de tudo. Por exemplo,
suponha que você queira fazer a correspondência da string 'First Name:'
seguida de todo e qualquer texto seguido de 'Last Name:' e, por fim, seguida
de qualquer caractere novamente. Podemos usar ponto-asterisco (.*) para
indicar “qualquer caractere”.
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1) # 'Al'
mo.group(2) # 'Sweigart'

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group() # '<To serve man>'
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group() # '<To serve man> for dinner.>'

# Correspondendo a quebras de linha com o caractere ponto
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# 'Serve the public trust.'
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

# Revisão dos símbolos de regex
'''
• ? corresponde a zero ou uma ocorrência do grupo anterior.
• * corresponde a zero ou mais ocorrências do grupo anterior.
• + corresponde a uma ou mais ocorrências do grupo anterior.
• {n} corresponde a exatamente n ocorrências do grupo anterior.
• {n,} corresponde a n ou mais ocorrências do grupo anterior.
• {,m} corresponde a zero até m ocorrências do grupo anterior.
• {n,m} corresponde a no mínimo n e no máximo m ocorrências do grupo
anterior.
• {n,m}? ou *? ou +? faz uma correspondência nongreedy do grupo anterior.
• ^spam quer dizer que a string deve começar com spam.
• spam$ quer dizer que a string dever terminar com spam.
• . corresponde a qualquer caractere, exceto os caracteres de quebra de linha.
• \d, \w e \s correspondem a um dígito, um caractere de palavra ou um
caractere de espaço, respectivamente.
• \D, \W e \S correspondem a qualquer caractere, exceto um dígito, um
caractere de palavra ou um caractere de espaço, respectivamente.
• [abc] corresponde a qualquer caractere que estiver entre os colchetes (por
exemplo, a, b ou c).
• [^abc] corresponde a qualquer caractere que não esteja entre os colchetes.
'''

# Correspondências sem diferenciar letras maiúsculas de minúsculas
regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
# 'RoboCop'
robocop.search('ROBOCOP protects the innocent.').group()
# 'ROBOCOP'
robocop.search('Al, why does your programming book talk about robocop so much?').group()
# 'robocop'

# Substituindo strings com o método sub()
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# A**** told C**** that E**** knew B**** was a double agent.'

# Administrando regexes complexas
'''
As expressões regulares serão convenientes se o padrão de texto para a
correspondência for simples. Porém fazer a correspondência de padrões
complicados de texto pode exigir expressões regulares longas e confusas.
'''
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?           # código de área
(\s|-|\.)?                   # separador
\d{3}                        # primeiros 3 dígitos
(\s|-|\.)                    # separador
\d{4}                        # últimos 4 dígitos
(\s*(ext|x|ext.)\s*\d{2,5})? # extensão
)''', re.VERBOSE)

# Combinando re.IGNORECASE, re.DOTALL e re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
