# DICIONÁRIOS
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.') # 'My cat has gray fur.'

spam = {12345: 'Luggage Combination', 42: 'The Answer'}

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon # False

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham # True - dicionários não são ordenados
# Pelo fato de não serem ordenados, os dicionários podem ser fatiados como as listas.


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == '':
		break
		
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have birthday information for ' + name)
		print('What is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('Birthday database updated.')


# MÉTODOS KEYS(), VALUES() E ITEMS()
spam = {'color': 'red', 'age': 42}
for v in spam.values():
	print(v)
# 42 | red 

for k in spam.keys():
	print(k)
# color | age 

for i in spam.items():
	print(i)
# ('color', 'red')
# ('age', 42)	
	
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
	print('Key: ' + k + ' Value: ' + str(v))
# Key: age Value: 42
# Key: color Value: red

spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()      # True
'Zophie' in spam.values()  # True
'color' in spam.keys()     # False
'color' not in spam.keys() # True
'color' in spam            # False

picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.' # 'I am bringing 2 cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' # 'I am bringing 0 eggs.'

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
# 'black'
print(spam) # {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white')
# 'black'
print(spam) # {'color': 'black', 'age': 5, 'name': 'Pooka'}

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1
print(count)
# {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i': 6, 
# 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p':1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}

# Apresentação elegante 
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)
# {' ': 13,',': 1,'.': 1,'A': 1,'I': 1,'a': 4,'b': 1,'c': 3,'d': 3,'e': 5,'g': 2,'h': 3,'i': 6,
# 'k': 2,'l': 3,'n': 4,'o': 2,'p': 1,'r': 5,'s': 3,'t': 6,'w': 2,'y': 1}

# pprint.pprint(someDictionaryValue)
# print(pprint.pformat(someDictionaryValue))

# Dicionários e listas aninhados
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
			 
def totalBrought(guests, item):
	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(item, 0)
	return numBrought
	
print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))