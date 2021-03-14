'''
Longest Collatz sequence
Problem 14
	
	The following iterative sequence is defined for the set of positive integers:
		n -> n/2 (n is even)
		n -> 3n + 1 (n is odd)
	Using the rule above and starting with 13, we generate the following sequence:
		13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 
		
	It can be seen that this sequence (starting at 13 and finishing at 1) contains
	10 terms. Although it has not been proved yet (Collatz Problem), it is thought
	thet all starting numbers finish at 1.
	
	Which starting number, under one million, produces the longest chain?
	
	NOTE: Once the chain starts the terms are allowed to go above one million.
'''
def addList(num):
	sequence.append(num)

def collatzSeq(num):
	if num == 1: 
		return 0
	else:
		if num%2 == 0: # se é par 
			num = num / 2 
			addList(num)
			collatzSeq(num)
		else:
			num = 3 * num + 1 
			addList(num)
			collatzSeq(num)
			
def sizeList(list):
	return len(list)

def testSize(newSize, notNewSize):
	if newSize > notNewSize:
		return newSize # retorna o maior tamanho 
	else:
		return notNewSize

NUM_MAX = 1000000
maxSize = 0

for i in range(NUM_MAX): # fará a sequencia a ser testada até 1000000
	i += 1 
	sequence = []
	collatzSeq(i)
	size = sizeList(sequence)
	maxSize = testSize(size, maxSize)
	i += 1 
	print(maxSize) # 524 
	
'''
é preciso confirmar essa resposta ainda
é possível fazer melhorias no programa 
no momento ele demora muito para obter o resultado
'''