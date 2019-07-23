
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
			
#collatzSeq(13)
#print(sequence)
#print(sizeList(sequence))
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