def hello():
	print('Hello')
	
hello() # 'Hello'

def hello(name):
	print('Hello ' + name)
	
hello('Alice') # Hello Alice
hello('Bob')   # Hello Bob

import random
def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain'
	elif answerNumber == 2:
		return 'It is decidedly so'
	elif answerNumber == 3:
		return 'Yes'
	elif answerNumber == 4:
		return 'Reply hazy try again'
	elif answerNumber == 5:
		return 'Ask again later'
	elif answerNumber == 6:
		return 'Concentrate and ask again'
	elif answerNumber == 7:
		return 'My reply is no'
	elif answerNumber == 8:
		return 'Outlook not so good'
	elif answerNumber == 9:
		return 'Very doubtful'
		
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
# forma compacta
print(getAnswer(random.randint(1, 9)))


# VALOR NONE - representa a ausência de valor
spam = print('Hello!') # Hello!
None == spam           # True 
# python acrescenta return None no final de qualquer definição de instrução que não tenha return 


# ARGUMENTOS NOMEADOS E PRINT()
print('Hello',end='')
print('World') 
# HelloWorld

print('cats', 'dogs', 'mice')          # cats dogs mice 
print('cats', 'dogs', 'mice', sep=',') # cats, dogs, mice


# ESCOPO LOCAL E GLOBAL
def spam():
	eggs = 'spam local'
	print(eggs) # 'spam local'
	
def bacon():
	eggs = 'bacon local'
	print(eggs) # 'bacon local'
	spam()      # 'spqm local'
	print(eggs) # 'bacon local'
	
bacon()
eggs = 'global'
bacon()
print(eggs) # 'global'


# TRATAMENTO DE EXCEÇÕES
'''
Até esse ponto, obter um erro, isto é, uma exceção em seu programa Python que dizer 
que o programa como um todo falhará. Queremos um programa que detecte erros, trate-os
e então continue a executar.
'''

def spam(devideBy):
	try:
		return 42 / devideBy
	except ZeroDivisionError:
		print('Error: Invalid argument.')
		
print(spam(2))  # 21.0 
print(spam(12)) # 3.5 
print(spam(0))  # Error: Invalid argument.
print(spam(1))  # 42.0


# ADIVINHE O NÚMERO
# Este é um jogo de adivinhar o número.
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Peça para o jogador adivinhar 6 vezes.
for guessesTaken in range(1, 7):
	print('Take a guess.')
	guess = int(input())

	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high.')
	else:
		break # Esta condição corresponde ao palpite correto!
		
if guess == secretNumber:
	print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Nope. The number I was thinking of was ' + str(secretNumber))
