'''
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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
		
primeNumbers = []
PRIME_MIN = 1000
PRIME_MAX = 9999

aux = True
i = PRIME_MIN
count = 0

while aux == True:
	if isPrime(i) == True:
		primeNumbers.append(i)
		count += 1 
	i += 2 
	if count == PRIME_MAX:
		aux = False
		break 
		
print(primeNumbers)
