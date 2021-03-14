'''
Circular primes
Problem 35

	The number, 197, is called a circular prime because all rotations of the 
	digits: 197, 971, and 719, are themselves prime.
	There are thirteen such primes below 100:
	2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

	How many circular primes are there below one million?
'''
NUM_MAX = 1000000

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

def reverseString(text):
    l = list(text)
    l.reverse()
    return ''.join(l)
	

primeList = []
count = 0 

for i in range(1, NUM_MAX):
	if isPrime(i) == True:
		#print(i)
		primeList.append(i)	
		
print(primeList)		

for i in primeList:
	i = str(i)
	#print(i)
	if isPrime(reverseString(str(i))) == True:
		count += 1 
		print(count)
		
print(count)
	
