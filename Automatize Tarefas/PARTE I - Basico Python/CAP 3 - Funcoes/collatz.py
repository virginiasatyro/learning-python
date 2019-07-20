def collatz(number):
	if number != 1:
		if number%2 == 0: # é par
			print(number/2)
			collatz(number/2)
		else: # é ímpar 
			print(3*number + 1)
			collatz(int(3*number + 1))
	else:
		return 1

import sys

while True:
	print('\nDigite um numero inteiro: ')
	try:
		num = input()
		num = int(num)
	except ValueError:
		print('Error: nao eh um numero inteiro, eh uma string!')
		sys.exit()
	response = collatz(num)
	if response == 1:
		sys.exit()