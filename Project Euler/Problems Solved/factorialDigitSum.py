'''
Factorial digit sum
Problem 20

	n! means n × (n − 1) × ... × 3 × 2 × 1

	For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
	and the sum of the digits in the number 10! is:
	3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

	Find the sum of the digits in the number 100!
'''
number = 100

def factorial(num):
	if num == 1:
		return num
	else:
		return num * factorial(num - 1)
		
def sumDigits(num):
	sum = 0
	num = str(num)
	for i in range(len(num)):
		sum = sum + int(num[i])
	return sum 
		
fact = factorial(number)
print(fact)
print(sumDigits(fact))