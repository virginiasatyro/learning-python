# Operadores: == != < > <= >=
# and or not 

name = 'Mary'
password = input()

if name == 'Mary':
	print('Hello Mary')

if password == 'swordfish':
	print('Access granted')
else:
	print('Wrong password')
	
name = 'Alice'
age = 25
if name == 'Alice':
	print('Hi, Alice!')
elif age < 12:
	print('You are not Alice, kiddo.')
elif age > 2000:
	print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
	print('You are not Alice, grannie')
	
	
spam = 0
if spam < 5:
	print('Hello world!')
	spam = spam + 1 
print(spam)	# 1 

spam = 0 
while spam < 5:
	print('Hello world')
	spam = spam + 1
print(spam)	# 5

name = ""
while name != 'virginia':
	print('Please, type your name.')
	name = input()
print('Thank you!')


while True:
	print('Please type your name.')
	name = input()
	if name == 'virginia':
		break;
		
print('Thank you!')