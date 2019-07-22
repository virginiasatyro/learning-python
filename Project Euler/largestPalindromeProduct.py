'''
Largest palindrome product 
Problem 4 

	A palindromic number reads the same both ways. The largest palindrome
	made from the product of two 2-digit numbers is 9009 = 91 x 99.
	Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(num):
	total_size = len(str(num))
	if total_size%2 == 0: # se é par 
		size = int(total_size/2)
	else:
		size = int(total_size/2) + 1

	for i in range(size): # 0 a size-1 
		str_num = str(num)
		if str_num[i] == str_num[total_size - 1 - i]: # é palíndromo
			result = True
		else:
			result = False
			break
	return result
	
products = []
MAX_DIG = 1000

for digit1 in range(MAX_DIG):
	for digit2 in range(MAX_DIG):
		product = digit1 * digit2
		if isPalindrome(product) == True: # é palíndromo 
			products.append(product)

products.sort()
print(products[-1]) # 906609