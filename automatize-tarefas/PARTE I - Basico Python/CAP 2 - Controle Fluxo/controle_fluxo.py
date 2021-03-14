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


print('My name is ')
for i in range(5):
	print('Jimmy Five times (' + str(i) + ')') # 0 1 2 3 4
	
# Gauss
total = 0
for num in range(101):
	total = total + num
print(total)

for i in range(12, 16):
	print(i) # Output: 12 13 14 15
	
for i in range(0, 10, 2):
	print(i) # Output: 0 2 4 6 8 
	
for i in range(5, -1, -1):
	print(i) # Output: 5 4 3 2 1 0
	
# IMPORTANDO MÓDULOS
import random 
for i in range(5): # randint - valor inteiro aleatório entre dois inteiros passados a ela 
	print(random.randint(1, 10)) # Output: 5 1 6 2 1 (random)
	
# SYS.EXIT() - programa é encerrado
import sys

while True:
	print('\nType exit to exit.')
	response = input()
	if response == 'exit':
		sys.exit()
	print('You typed ' + response + ' .')