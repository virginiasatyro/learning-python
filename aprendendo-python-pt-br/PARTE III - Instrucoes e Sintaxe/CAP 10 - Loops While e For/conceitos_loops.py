# LOOPS WHILE
'''
while <teste>:    # faz um loop em teste 
	<instruções1> # miolo do loop
else:             # else opcional 
	<instruções2> # executadas se não saiu do loop com break
'''

x = 'spam'
while x:
	print (x),
	x = x[1:] # retira o primeiro caractere de x 
# spam pam am m 

a = 0; b = 10
while a < b: # uma maneira de codificar loops contadores
	print (a),
	a += 1   # ou a = a + 1 
# 0 1 ... 9 


# BREAK,  CONTINUE, PASS E A CLÁUSULA ELSE
# BREAK: sai do loop mais próximo que a envolve;
# CONTINUE: pula para o início do loop mais próximo que a envolve;
# PASS: não faz absolutamente nada; trata-se de um lugar reservado de instrução, vazio;
# ELSE do loop: é executado se, e somente se, saímos do loop normalmente - sem atingir uma instrução break;

# -> Formato de loop geral
'''
while <teste1>:
	<instruções1>
	if <teste2>: break    # sai do loop agora, pula a cláusula else 
	if <teste3>: continue # vai para o início do loop agora 
else:
	<instruções2>         # se não atingimos uma instrução 'break'
'''

# while 1: pass # digite ctrl-c para interromper

x = 10
while x:
	x = x - 1                 
	if  x % 2 != 0: continue # ímpar? pula a impressão
	print (x)

x = 10 
while x:
	x = x - 1 
	if x % 2 == 0: # par? imprime 
		print (x)

''' raw_input (não está funcionando)
while 1:
	name = raw_input('Enter name:')
	if name == 'stop': break 
	age = raw_input('Enter age: ')
	print ('Hello'), (name), ('=>'), (int(age) ** 2)
''' 

y = 20
x = y / 2 
while x > 1:
	if y % x == 0:                     # resto 
		print (y), ('has factor'), (x)
		break                          # pula a cláusula else 
	x = x - 1 
else:                                  # saída normal 
	print (y), ('is prime')
	
'''
found = 0
while x and not found:
	if match(x[0]): # o valor está no início?
		print ('Ni')  
		found = 1 
	else:
		x = x[1:]   # fraciona o início e repete 
if not found:
	print ('not found')
'''


# LOOPS FOR
'''
for <destino> in <objeto>: #atribui itens do objeto ao destino 
	<instruções>           # miolo do loop repetido: usa o destino 
else:
	<instruções>           # se não atingirmos uma instrução 'break'
'''

for x in ["spam", "eggs", "ham"]:
	print (x) # spam eggs ham

sum = 0
for x in [1, 2, 3, 4]:
	sum = sum + x 
print (sum) # = 10 

prod = 1 
for item in[1, 2, 3, 4]: prod *= item 
print (prod) # = 24

S, T = "lumberjack", ("and", "I,m", "okay")
for x in S: print (x) # = l u m b e r j a c k 
for x in T: print (x) # and I'm okay 

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
	print (a , b)

items = ["aaa", 111, (4, 5), 2.01] # um conjunto de objetos
tests = [(4, 5), 3.14]             # chaves para pesquisar
for key in tests:                  # para todas as chaves
	for item in items:              # para todos os itens 
		print (key, "was found!")
		break
	else:
		print (key, "not found!")
# = (4, 5) was found
# = 3.14 was found

for key in tests:
	if key in items:
		print (key, "was found!")
	else:
		print (key, "not found!")

seq1 = "spam"
seq2 = "scam"
rec = []              # começa vazio
for x in seq1:        # percorre a primeira sequência
	if x in seq2:     # item comum?
		rec.append(x) # adiciona no final do resultado
print (rec) # = ['s', 'a', 'm']


# VARIAÇÕES DE LOOPS
# -> Loops contadores: range 
range(5)        # [0, 1, 2, 3, 4]
range(2, 5)     # [2, 3, 4]
range(0, 10, 2) # [0, 2, 4, 6, 8]

# -> Varredores de arquivo
file = open('test.txt', 'r')
# print file.read()

file = open('test.txt')
while 1:
	char = file.read(1) # lê por caractere
	if not char: break
	print (char)

for char in open('test.txt').read():
	print (char)

file = open('test.txt')
while 1:
	line = file.readline() # lê linha por linha
	if not line: break
	print (line),

file = open('test.txt', 'rb')
while 1:
	chunk = file.read(10) # lê trechos de bytes 
	if not chunk: break
	print (chunk),
# = b'1 \r\n2 \r\n3 '
# = b'\r\ntestando'

'''
for line in open('test.txt').readlines(): print line
for line in open('test.txt').xreadlines(): print line
for line in open('test.txt'): print line
'''

range(-5, 5)     # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
range(5, -5, -1) # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

for i in range(3):
	print (i, 'Pythons') # 0 Pythons 1 Pythons ...
	
X = 'spam'
for item in X: print (item) # iteração simples

i = 0
while i < len(X): # iteração do loop while  (mesmo resultado da iteração anterior)
	print (X[i]); i += 1 

X                                    # 'spam'
len(X)                               # 4 
range(len(X))                        # [0, 1, 2, 3]
for i in range(len(X)): print (X[i]) # indexação de loop for manual 

# -> Varreduras não exaustivas: range 
S = 'abcdefghijk'
range(0, len(S), 2)                        # [0, 2, 4, 6, 8, 10]
for i in range(0, len(S), 2): print (S[i]) # a c e g i k 

# -> Alterando listas: range
L = [1, 2, 3, 4, 5]
for i in range(len(L)): # soma um a cada item em L 
	L[i] += 1           # ou L[i] = L[i] + 1 
print (L)               # = [2, 3, 4, 5, 6]

i = 0 
while i < len(L):
	L[i] += 1 
	i += 1 
print (L)

# -> Varreduras paralelas: zip e map
# ZIP - permite usar loops for para visitar várias sequências em paralelo
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
zip(L1, L2) # [(1, 5), (2, 6), (3, 7), (4, 8)]

for(x, y) in zip(L1, L2):
	print (x, y, '--', x + y)
# 1 5 -- 6 
# 2 6 -- 8

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
T3
zip (T1, T2, T3) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

S1 = 'abc'
S2 = 'xyz123'
zip(S1, S2) # [('a', 'x'), ('b', 'y'), ('c', 'z')]

# MAP - cria pares de itens de sequências de maneira semelhante, mas preenche as sequências mais curtas com None
map(None, S1, S2) # [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]

# -> Construção de dicionário com zip
D1 = {'spam': 1, 'eggs': 3, 'toast': 5}
print (D1)
D1 = {}
D1['spam'] = 1 
D1['eggs'] = 3 
D1['toast'] = 5 

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
zip(keys, vals) # [('spam', 1), ('eggs', 3), ('toast', 5)]
D2 = {}
for (k, v) in zip(keys, vals) : D2[k] = v 
print (D2)

# construindo o dicionário sem o for (mais fácil)
keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
D3 = dict(zip(keys, vals))
print (D3) # [('spam', 1), ('eggs', 3), ('toast', 5)]