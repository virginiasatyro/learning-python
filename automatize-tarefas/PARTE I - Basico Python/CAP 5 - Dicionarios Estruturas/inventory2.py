'''
é preciso fazer uma correção
no momento o programa só aceita adicionar um tipo de item que não estava na lista'''

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(invent):
	count = 0;
	print('Inventory:')
	for k, v in invent.items():
		print(str(v) + ' ' + k)
		count = count + v
	print('Total number of items: ' + str(count) + '\n')
	
displayInventory(inventory)

def addToInventory(invent, addedItems):
	addItem = []
	for i in addedItems:
		item = i
		
		for k, v in invent.items():
			if(item == k): # se o item já existe no inventário 
				v += 1 
				invent[k] = v
			else: # item não estava presente no inventário
				# addItem.insert(0, k)
				addItem = item 
	invent[addItem] = 1
	'''for j in range(len(addItem)):
		invent[addItem[j]] = 1
		print(addItem[j])
				'''
	return invent


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'algo'] # lista de strings
inventory2 = addToInventory(inventory, dragonLoot)
displayInventory(inventory2)


'''
Função de “lista para dicionário” para o inventário de jogo de
fantasia
Suponha que os despojos de um dragão vencido seja representado como uma
lista de strings como esta:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Crie uma função chamada addToInventory(inventory, addedItems), em que
o parâmetro inventory seja um dicionário representando o inventário do
jogador (como no projeto anterior) e o parâmetro addedItems seja uma lista
como dragonLoot. A função addToInventory() deve retornar um dicionário
que represente o inventário atualizado. Observe que a lista addedItems pode
conter vários itens iguais. Seu código poderá ser semelhante a:
def addToInventory(inventory, addedItems):
# seu código deve ser inserido aqui
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

O programa anterior (com sua função displayInventory() do projeto
anterior) apresentará a saída a seguir:
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
'''