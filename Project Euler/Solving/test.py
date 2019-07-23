aux = True
triangleSeq = []
i = 1 
triangleNum = 0 
MAX_DIVISOR = 501 

def quantDivisors(num):
	divisors = []
	for i in range(num):
		i += 1 
		if num%i == 0: # é um divisor 
			divisors.append(i)
	return len(divisors)

while aux == True:
	triangleNum = triangleNum + i 
	# triangleSeq.append(triangleNum)
	i += 1 
	
	if quantDivisors(triangleNum) >= MAX_DIVISOR:
		aux = False
		break

print(triangleNum)
