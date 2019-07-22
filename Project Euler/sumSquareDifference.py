'''
Sum square difference
Problem 6 

	The sum of the squares of the first ten natural numbers is,
	1^2 + 1^2  + ... + 10^2 = 385 
	The square of the sum of the first ten natural numbers is 
	(1 + 2 + ... + 10)^2 = 55^2 = 3025 
	Hence the difference between the sum of the squares of the first ten natural
	numbers and the square of the sum is 3025 - 385 = 2640 
	
	Find the difference between the sum of the squares of the first one hundred 
	natural numbers and the square of the sum.
'''

NUM_MAX = 100

def sumSquare(num):
	sum = 0 
	for i in range(num):
		i += 1
		sum = sum + i * i 
	return sum 

def squareSum(num):
	sum = 0 
	for i in range(num):
		i += 1 
		sum = sum + i 
	sum = sum * sum 
	return sum
	
print(sumSquare(NUM_MAX))
print(squareSum(NUM_MAX))
print(squareSum(NUM_MAX) - sumSquare(NUM_MAX)) # 25164150