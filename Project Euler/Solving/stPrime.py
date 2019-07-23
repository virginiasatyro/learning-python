'''
10001st prime 
Problem 7

	By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can 
	see that the 6th prime is 13.
	
	What is the 10001st prime number?
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
		
primeNumbers = [2]
PRIME_MAX = 10001
aux = True
count = 0 
i = 3 

while aux == True:
	if isPrime(i) == True:
		primeNumbers.append(i)
		count += 1
	i += 2 
	if count == PRIME_MAX - 1:
		aux = False
		break 
	
print(primeNumbers)
print(primeNumbers[-1]) # 104743