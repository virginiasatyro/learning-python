# FUNÇÕES ANÔNIMAS: LAMBDA
# Além da instrução DEF, Python também fornece uma forma de expressão que gera objetos função;
# LAMBDA - cria uma função para ser chamada posteriormente, mas a retorna, em vez de atribuir
# um nome a ela;
# Frequentemente usadas como uma maneira de colocar uma definição de função em linha ou adiar
# a execução de um trecho de código;
# lambda argumento1, argumento2, ... argumentoN: expressão usando argumentos
# * LAMBDA é uma expressão e não uma instrução;
# * O miolo de LAMBDA é uma única expressão e não um bloco de instruções;

def func(x, y, z): return x + y + z 
print(func(2, 3, 4)) # = 9

# é possível obter o mesmo efeito com uma expressão LAMBDA, atribuindo um resultado explicitamente a um nome:
f = lambda x, y, z: x + y + z 
print(f(2, 3, 4)) # = 9

x = (lambda a = "fee", b = "fie", c = "foe": a + b + c)
print(x("wee")) # = weefiefoe

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = knights()
print(act('Robin')) # = Sir Robin

'''
As expressões LAMBDA são úteis como uma espécie de atalho de função que permite incorporar
a definição de uma função dentro do código que a utiliza.
São comumente usadas para desenvolver tabelas de salto - listas ou dicionários de ações a 
serem executadas de acordo com a demanda.
'''
L = [(lambda x: x**2), (lambda x: x**3), (lambda x: x**4)]
for f in L:
    print (f(2)) # = 4, 8, 16
print (L[0](3))  # = 9

key = 'got'
{'already': (lambda: 2 + 2),
'got':      (lambda: 2 * 4),
'one':      (lambda: 2**6)
}[key]() # = 8


# COMO (NÃO) OFUSCAR SEU CÓDIGO PYTHON
# É possível simular uma instrução IF combinando operadores booleanos em expressões
a, b, c = 1, 0, 1
((a and b) or c)
# é aproximadamente equivalente a:
if a:
    b
else:
    c 

# AND e OR são de curto-circuito - não avaliam o lado direiro se o esquerdo determinar o resultado
t, f = 1, 0
x, y = 88, 99
a = (t and x) or y # se for verdadeiro, x
print (a) # = 88 
a = (f and x) or y # se for falso, y 
print (a) # = 99 
# só funciona caso tenha certeza de que x não será falso também
# Para simular realmente IF - envolver dois resultados possíveis, de modo a torná-los não falsos, e
# então indexar para extrair o resultado no fim:
'''
((t and [x] or [y])[0]  # se for verdadeiro, x 
((f and [x] or [y])[0]  # se for falso, y 
(t and f) or y          # falha: f é falso, pulado 
((t and [f]) or [y])[0] # funciona: f é retornado de qualquer maneira 
'''
	
def ifelse(a, b, c): 
    return ((a and [b]) or [c])[0]
   
print(ifelse(1, 'spam', 'ni')) # = spam 
print(ifelse(0, 'spam', 'ni')) # = ni 

import sys
showball = (lambda x: map(sys.stdout.write, x))
t = showball(['spam\n', 'toast\n', 'eggs\n'])
# = spam toast eggs 

# Expressões LAMBDA aninhadas e escopos
def action(x):
    return (lambda y: x + y)

act = action(99)
print(act(2)) # = 101


# APLICANDO FUNÇÕES A ARGUMENTOS 
# Função interna: APPLY
'''
def func(x, y, z): 
    return x + y + z 
	
apply(func, (2, 3, 4)) # = 9 aparentemente não funciona em Python 3
f = lambda x , y, z: x + y + z 
apply(f, (2, 3, 4)) # = 9 
''' 


# FUNÇÕES DE MAPEAMENTO SOBRE SEQUÊNCIAS
counters = [1, 2, 3, 4]
update = []
for x in counters:
    update.append(x + 10) # soma 10 a cada item 

print(update) # = [11, 12, 13, 14]

# MAP - aplica uma função passada a cada  item de um objeto sequência, e retorna uma 
# lista contendo todos os resultados de chamada de função;
def inc(x):
    return x + 10 

map(inc, counters)               # coleta os resultados = [11, 12, 13, 14]
map((lambda x: x + 3), counters) # expressão de função = [4, 5, 6, 7]

# utilitário de mapeamento geral
def mymap(func, seq):
    res = []
    for x in seq: 
        res.append(func(x))
    return res

# MAP - função interna é mais rápida	
map(inc, [1, 2, 3])   # = [11, 12, 13]
mymap(inc, [1, 2, 3]) # = [11, 12, 13]

print(pow(3, 4))               # 81
map(pow, [1, 2, 3], [2, 3, 4]) # [1, 8, 81]


# FERRAMENTAS DE PROGRAMAÇÃO FUNCIONAL
range(-5, 5)                            # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
filter((lambda x: x > 0), range(-5, 5)) # [1, 2, 3, 4]

# seria equivalente a escrever:
res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)
	
print(res) # [1, 2, 3, 4]

'''
Função REDUCE aparentemente não está definida em Python 3
'''


# ABRANGÊNCIA DE LISTA
# ODR - retorna o código ASCII inteiro de um único caractere
print(ord('s')) # = 115
# CHR - retorna o caractere de um inteiro em código ASCII
print(chr(115)) # = s 

res = []
for x in 'spam': # coletar todos os ASCII de uma string
    res.append(ord(x))

print(res) # [115, 112, 97, 109]

# podemos utilizar a função MAP:
res = map(ord, 'spam')
res # [115, 112, 97, 109]

# podemos utilizar expressão de abrangência de lista:
res = [ord(x) for x in 'spam'] # aplica expressão na sequência
print(res) # [115, 112, 97, 109]

[x**2 for x in range(10)]        # [0, 1, 2, 4, 9, 16, 25, 36, 49, 64, 81]
map((lambda x: x**2), range(10)) # [0, 1, 2, 4, 9, 16, 25, 36, 49, 64, 81]

# Adicionando testes e loops aninhados:
print([x for x in range(5) if x%2 == 0]) # [0, 2, 4]
filter((lambda x: x%2 == 0), range(5))   # [0, 2, 4]
res = []
for x in range(5):
    if x%2 == 0: res.append(x)
print(res) # [0, 2, 4]

[x**2 for x in range(10) if x%2 == 0]                          # [0, 4, 16, 36, 64]
map((lambda x: x**2), filter((lambda x: x%2 == 0), range(10))) # [0, 4, 16, 36, 64]

'''
Estrutura geral das abrangências de lista:
[expressão for destino1 in sequência1 [if condição]
           for destino2 in sequência2 [if condição]
           ...
           for destinoN in sequênciaN [if condição]]
'''

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res) # [100, 200, 300, 101, 201, 301, 102, 202, 302]

res = [x + y for x in 'spam' for y in 'SPAM']
print(res) # ['sS', 'sP', 'sA', 'sM', 'pS', 'pP', 'pA', 'pM', 'aS', 'aP', 'aA', 'aM', 'mS', 'mP', 'mA', 'mM']

res = [(x, y) for x in range(5) if x%2 == 0 for y in range(5) if y%2 == 1]
print(res) # [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

# Importancia de MAP e ABRANGÊNCIA
print(open('myfile.txt').readlines())                         # ['aaa\n', 'bbb\n', 'ccc\n']
print([line[:-1] for line in open('myfile.txt').readlines()]) # ['aaa', 'bbb', 'ccc']
print([line[:-1] for line in open('myfile.txt')])             # ['aaa', 'bbb', 'ccc']
map((lambda line: line[:-1]), open('myfile.txt'))             # ['aaa', 'bbb', 'ccc']
# Os 2 últimos utilizam ITERADORES DE ARQUIVO


# FUNÇÕES GERADORAS DE ITERADORES
# Expressão de função geradora:
def gensquares(N):
    for i in range(N):
        yield i ** 2 # retoma aqui posteriormente

for i in gensquares(5): # retoma a função
    print(i)            # 0 1 4 9 16
	
x = gensquares(10)
print(x) # <generator object gensquares at 0x00000252C27F62B0>
'''
Aparentemente next não funciona em Python 3 
x.next() # = 0 
x.next() # = 1 
'''

# Tmabém poderíamo construir de uma vez toda a lista de valores produzidos:
def buildsquares(n):
    res = []
    for i in range(n): res.append(i**2)
    return res 

for x in buildsquares(5): print(x) # 0 1 4 9 16

# E também:
for x in [n**2 for n in range(5)]:
    print (x) # 0 1 4 9 16

for x in map((lambda x : x**2),  range(5)):
    print(x) # 0 1 4 9 16

# Iteradores e tipos internos
D = {'a': 1, 'b': 2, 'c': 3}
x = iter(D)
# x.next()

for key in D:
    print(key, D[key]) # a 1 / c 3 / b 2


# CONCEITOS DE PROJETO DE FUNÇÃO
'''
* Acoplamento: use argumentos para entradas e retorno para saídas;
* Acoplamento: use variáveis globais apenas quando forem realmente necessárias;
* Acoplamento: não altere argumentos mutáveis a não ser que quem fez a chamada espere isso;
* Coesão: cada função deve ter um só propósito unificado;
* Tamanho: cada função deve ser relativamente pequena;
'''

# As funções são objetos: chamadas indiretas
def echo(message): # eco atribuído a um objeto função 
    print(message)

x = echo           # agora x faz referência a ele também 
x('Hello world!')  # chama o objeto adicionado () = Hello world!

def indirect(func, arg):
    func(arg) # chama os objetos adicionando ()

indirect(echo, 'Hello jello!') # passa função para um função = Hello jello!

schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
for(func, arg) in schedule:
    func(arg) # = Spam! Ham!
	

# PROBLEMAS DAS FUNÇÕES
# Os nomes locais são detectados estaticamente

x = 99 
def selector(): # x usado mas não atribuído 
    print (x)   # x encontrado no escopo global     

selector() # = 99 -> deveria ser esse valor? Não!

'''
def selector():
    print(x) # ainda não existe!
    x = 88   # x classificado como nome local (por toda parte)

selector()
ERRO!
File "conceitos_funcoes_avancados.py", line 289, in selector
print(x) # ainda não existe!
UnboundLocalError: local variable 'x' referenced before assignment
'''

def selector():
    global x # força x a ser global (por toda parte)
    print(x) # = 99 
    x = 88 
    print(x) # = 88 

selector()

y = 99 
def selector():
    import __main__
    print(__main__.y) # 99 
    x = 88 
    print(x)          # 88 

selector()

# Padrões e objetos mutáveis:
def saver(x = []): # salva um objeto lista
    x.append(1)    # altera o mesmo objeto a cada vez 
    print(x)

saver([2]) # padrão não usado = [2, 1] 
saver()    # padrão usado = [1]
saver()    # cresce a cada chamada! = [1, 1]
saver()    # [1, 1, 1]
# 'padões mutáveis são difíceis de lembrar e entender!'

def saver(x = None):
    if x is None: # nenhum argumento passado?
        x = []    # executa código para fazer uma nova lista 
    x.append(1)   # altera o novo objeto lista 
    print(x)

saver([2]) # [2, 1]
saver()    # não cresce aqui = [1]
saver()    # [1]

# Funções sem retorno:
def proc(x):
    print(x) # nenhum retorno é um retorno None 

x = proc('testing 123...') # testing 123...
print (x) # None 

list = [1, 2, 3]
list = list.append(4) # append é uma "procedure"
print(list) # = None