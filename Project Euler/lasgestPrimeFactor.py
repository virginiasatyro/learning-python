'''
Largest prime factor
Problem 3 

	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143?
'''

number = 600851475143
divisors = []
evenDivisors = [1]

for i in range(number):
	i += 1
	if number%i == 0: # é um divisor 
		divisors.append(i)
	
	
def isPrime(list):
	for i in range(len(list)): # percorre cada membro da lista 
		count = 0
		for j in range(list[i]):
			j += 1
			if list[i]%j == 0:
				count += 1 
			if count > 3:
				break
		if count == 2:
			evenDivisors.append(list[i])
	
	return evenDivisors

isPrime(divisors)
print(evenDivisors)
largestPrimeFactor = evenDivisors[-1]
print(largestPrimeFactor)