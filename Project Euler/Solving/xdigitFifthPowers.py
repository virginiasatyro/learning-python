'''
Digit fifth powers
Problem 30

	Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

		1634 = 1^4 + 6^4 + 3^4 + 4^4
		8208 = 84 + 24 + 04 + 84
		9474 = 94 + 44 + 74 + 44

	As 1 = 14 is not a sum it is not included.
	The sum of these numbers is 1634 + 8208 + 9474 = 19316.

	Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
def numDigits(num):
	num = str(num)
	return len(num)
	
def digitPower(num, p):
	num = str(num)
	sum = 0
	for i in range(4):
		sum = sum + (int(num[i]))**p
	return sum 
	
NUM_MAX = 9999 
power = numDigits(NUM_MAX)
print(digitPower(8208, 4))
list = []
total_sum = 0 

for j in range(1, NUM_MAX):
	aux = digitPower(j, 4)
	if j == aux:
		total_sum = total_sum + aux
		list.append(aux)

print(list)
print(total_sum)