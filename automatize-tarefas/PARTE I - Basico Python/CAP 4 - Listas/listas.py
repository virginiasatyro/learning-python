[1, 2, 3]
['cat', 'bat', 'rat']
['hello', 3.1415, True, None, 42]

spam = ['cat', 'bat', 'rat']
print(spam)    # ['cat', 'bat', 'rat']
print(spam[0]) # cat

spam = [['cat', 'bat'], [10, 20, 30, 40]]
print(spam[0])    # ['cat', 'bat']
print(spam[1][3]) # 40

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])  # elephant
print(spam[-3])  # bat
print(spam[1:3]) # ['bat', 'rat']
print(len(spam)) # 4

[1, 2, 3] + ['A', 'B', 'C']   # [1, 2, 3, 'A', 'B', 'C']
['X', 'Y', 'Z'] * 3           # ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C'] # [1, 2, 3, 'A', 'B', 'C']

del spam[0] # [2, 3, 'A', 'B', 'C']

catNames = []
while True:
	print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
	name = input()
	if name == '':
		break
	catNames = catNames + [name] # concatenação de lista

print('The cat names are:')
for name in catNames:
	print(' ' + name)


supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
# Index 0 in supplies is: pens | Index 1 in supplies is: staplers | Index 2 in supplies is: flame-throwers | Index 3 in supplies is: binders	
	
print('howdy' in ['hello', 'hi', 'howdy', 'heyas']) # True
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam     # False
'cat' not in spam # True
	
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# você pode digitar a linha de código a seguir:
cat = ['fat', 'black', 'loud']


# MÉTODOS
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello')) # 0
spam.index('heyas')        # 3
# spam.index('howdy howdy howdy') ERRO

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam) # ['cat', 'dog', 'bat', 'moose']

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam) # ['cat', 'chicken', 'dog', 'bat']

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam) # ['cat', 'rat', 'elephant']

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam) # ['bat', 'rat', 'cat', 'hat', 'cat']

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam) # [-7, 1, 2, 3.14, 5]

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam) # ['ants', 'badgers', 'cats', 'dogs', 'elephants
spam.sort(reverse=True)
print(spam) # ['elephants', 'dogs', 'cats', 'badgers', 'ants']

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam) # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam) # ['a', 'A', 'z', 'Z']
	
# Magic Ball 8
import random
messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])

print('Four score and seven ' + \
'years ago...')

name = 'Zophie'
name[0]         # 'Z'
name[-2]        # 'i'
name[0:4]       # 'Zoph'
'Zo' in name    # True
'z' in name     # False
'p' not in name # False
for i in name:
	print('* * * ' + i + ' * * *')
# * * * Z * * *
# * * * o * * *
# * * * p * * *
# * * * h * * *
# * * * i * * *
# * * * e * * *
	
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)    # 'Zophie a cat'
print(newName) # 'Zophie the cat'	
	
eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs) # [4, 5, 6]
	
eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs) # [4, 5, 6]
	
	
# TUPLA
# as tuplas, assim como as strings, são imutáveis
eggs = ('hello', 42, 0.5)
print(eggs[0])   # 'hello'
print(eggs[1:3]) # (42, 0.5)
print(len(eggs)) # 3 

type(('hello',)) # <class 'tuple'>
type(('hello'))  # <class 'str'>

tuple(['cat', 'dog', 5]) # ('cat', 'dog', 5)
list(('cat', 'dog', 5))  # ['cat', 'dog', 5]
list('hello')            # ['h', 'e', 'l', 'l', 'o']
	

spam = 42
cheese = spam
spam = 100
spam   # 100
cheese # 42

# Atenção! Passagem por referência!
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
spam   # [0, 'Hello!', 2, 3, 4, 5]
cheese # [0, 'Hello!', 2, 3, 4, 5]

def eggs(someParameter):
	someParameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam) # [1, 2, 3, 'Hello']

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
spam   # ['A', 'B', 'C', 'D']
cheese # ['A', 42, 'C', 'D']

# Se a lista contiver listas, utilize a função copy.deepcopy() no lugar de copy.copy().
# A função deepcopy() copiará essas listas internas também.