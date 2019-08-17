'''
Digit factorials
Problem 34

	145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

	Find the sum of all numbers which are equal to the sum of the factorial of their digits.

	Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

#number = 145

'''def factorial(num):
	if num == 1:
		return num
	else:
		return num * factorial(num - 1)'''
def factorial(num):
	result = 1 
	for i in range(num):
		result = result * (num - i)
	return result 
		
def sumDigitsFact(num):
	sum = 0
	num = str(num)
	for i in range(len(num)):
		sum = sum + factorial(int(num[i]))
	return sum 
		
#result = sumDigitsFact(number)
#print(result)

total_sum = 0
for i in range(3, 100000):
	aux = sumDigitsFact(i)
	if aux == i: 
		total_sum = total_sum + aux 

print(total_sum) # 40730

''' 
é possível melhorar o algoritmo
mas como saber até que numero é o maximo? 
sabendo que é abaixo de 100000
'''