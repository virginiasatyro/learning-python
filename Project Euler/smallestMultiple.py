'''
Smallest multiple
Problem 5 

	2520  is the smallest number that can be divided by each of the numbers
	from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible by all of
	the numbers from 1 to 20?
'''
NUM = 20

def smallest():
	number = NUM
	while True:
		for i in range(NUM):
			i += 1 
			if number%i == 0:
				if i == NUM:
					return number
			else:
				break 
		number += NUM

number = smallest()		
print(number) # 232792560