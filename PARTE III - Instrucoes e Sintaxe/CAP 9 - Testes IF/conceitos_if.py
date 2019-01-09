# INSTRUÇÕES IF
'''
if <teste1>:    # teste  if 
<instruções1>   # bloco associado
elif <teste2>:  # instruções elif opcionais 
<instruções2>
else:           # instrução else opcional
<instruções3> 
'''

if 1:
	print ('true')
	
	
if not 1:
	print ('true')
else:
	print ('false')
	
	
x = 'killer rabbit'
if x == 'roger':
	print ("how's jessica?")
elif x == 'bugs':
	print ("what's up doc?")
else:
	print ('Run away! Run away!')
	
# -> Desvio de vários caminhos
choice = 'ham'
print ({'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}[choice]) # = 1.99

branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}
print (branch.get('spam', 'Bad choice'))  # = 1.25 
print (branch.get('bacon', 'Bad choice')) # = Bad choice


# REGRAS DE SINTAXE DO PYTHON
'''
* As instruções são executadas uma após a outra, até que você diga o contráario;
* Os limites de blocos e de instruções são detectados automaticamente;
* Instruções compostas = cabeçalo. ":", instruções endentadas;
* Normalmente, linhas em branco, espaços e comentários são ignorados;
* As strings de documentação são ignoradas, mas são salvas e exibidas por ferramentas;
'''

# -> Delimitadores de bloco
# Python detecta os limites automaticamente pela endentação da linha - espaço vazio à esquerda do código;
x = 1
if x:
	y = 2
	if y:
		print ('bloco2')
	print ('bloco1')
print ('bloco0')

# -> Delimitadores de instrução
# * as instruções podem abranger várias linhas se você estiver continuando um par sintático aberto;
# * as instruções podem abranger várias linhas se terminarem com uma barra invertida;

# -> Alguns casos especiais:
L = {"Good", # pares abertos podem abranger várias linhas
"Bad",
"Ugly"}

'''
if a == b and c == d and \ # barras invertidas permitem continuações
d == e and f == g:
	print ('olde')
''' # não funciona em Python 3?

if (a == b and c == d and # parênteses normalmente também são permitidos
d == e and f == g):
	print ('new')
	
x = 1; y = 2; print x # mais de uma instrução simples

if 1: print ('hello') # instrução simples na linha de cabeçalo


# TESTES DE VERDADE
'''
x and y
x or y 
not x 
'''
2 < 3, 3 < 2   # (1, 0)
2 or 3, 3 or 2 # retorna o operando da esquerda se for verdadeiro = (2, 3)
# senão, retorna o operando da direita (verdadeiro ou falso)
[] or 3  # = 3
[] or {} # = {}

2 and 3, 3 and 2 # retorna o operando da esquerda se for falso = (3, 2)
# senão, retorna o operando da direita (verdadeiro ou falso)
[] and {} # []
3 and []  # []