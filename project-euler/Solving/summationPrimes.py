'''
Summation of primes
Problem 10

	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	
	Find the sum of all the primes below two million.
'''

def isPrime(num):
	count = 0 
	for i in range(num):
		i += 1
		if num%i == 0:
			count += 1 
		if count > 3:
			return False
			break
	if count <= 2:
		return True
	else:
		return False 
		
PRIME_MAX = 2000000
primeNumbers = [2]
aux = True 
i = 3 

while aux == True:
	if i >= PRIME_MAX:
		aux = False
		break
	else:	
		if isPrime(i) == True:
			primeNumbers.append(i)
		i += 2 
			
print(primeNumbers)			

def sumPrimes(list):
	sum = 0
	for i in range(len(list)):
		sum += list[i] 
	return sum 
	
print(sumPrimes(primeNumbers))