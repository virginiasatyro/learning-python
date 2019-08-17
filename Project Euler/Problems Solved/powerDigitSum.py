'''
Power digit sum
Problem 16

	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

	What is the sum of the digits of the number 2^1000?
'''

def powerDigits(num):
	power = 2**num 
	sum = 0
	power = str(power)
	print(power)
	for i in range(len(power)):
		sum = sum + int(power[i])
	return sum 
	
print(powerDigits(1000)) # 1366