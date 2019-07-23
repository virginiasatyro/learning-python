''' 
Multiples of 3 and 5 
Problem 1

	If we list all the natural numbers below 10 that are multiples 
	of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.
'''

NUM_MAX = 1000 # numero máximo
sum = 0        # soma do total 

for i in range(NUM_MAX):
	if i%3 == 0:   # divisível por 3 
		sum += i
	elif i%5 == 0: # divisível por 5 
		sum += i 

print(sum) # 233168