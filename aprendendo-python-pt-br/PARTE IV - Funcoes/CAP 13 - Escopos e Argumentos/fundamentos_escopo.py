# REGRAS DE ESCOPO

# * O módulo envolvente é um escopo global;
# * O escopo global abrange apenas um arquivo;
# * Cada chamada para uma função é um novo escopo local;
# * Os nomes atribuídos são locais, a não ser que sejam declarados como globais;
# * Todos os outro nomes são locais, globais ou internos envolventes;

'''
Solução de nome: a regra LEGB
* As referências de nome pesquisam no máximo quatro escopos: local, em seguida as funções
envolventes (se houver), depois global e, então, interno;
* As atribuições de nome criam ou alteram nomes locais, por padrão;
* As declarações globais fazem o mapeamento dos nomes atribuídos para o escopo de um módulo envolvente;
L - local 
E - envolventes 
G - global 
B - built-in 
'''

# Exemplo de escopo
# Escopo global
x = 99         # x e func atribuídos no módulo: globais 

def funct(y):  # y e z atribuídos na função~: locais 
    # escopo local
	z = x + y  # x é global
	return z

print(funct(1)) # func no módulo: resultado = 100

# Escopo interno 
# Módulo da biblioteca padrão previamente construído, chamado __builtin__, que você pode importar se quiser ver quais nomes são predefinidos;
import builtins
print(dir(builtins))
# os nomes da lista são o escopo interno do Python

# INSTRUÇÃO GLOBAL
# * GLOBAL significa "um nome no nível superior do arquivo de módulo envolvente";
# * Os nomes globais só devem ser declarados se forem atribuídos´em uma função;
# * Os nomes globais podem ser referenciados em uma função sem serem declarados;

y, z = 1, 2
def all_global():
    global x 
    x = y + z 
	
# ESCOPOS E FUNÇÕES ANINHADAS
def f1():
    x = 88
    def f2():
        print (x)
    f2()
f1() # imprime 88

def f1():
    x = 88
    def f2():
	    print (x)
    return f2 
action = f1() # faz e retorna uma função 
action()      # agora, a chama: imprime 88


# PASSANDO ARGUMENTOS
# * Os argumentos são passados pela atribuição automática de objetos a nomes locais;
# * A atribuição de nomes de argumento dentro de uma função não afeta quem fez a chamada;
# * A alteração de um argumento de objeto mutável em uma função pode ter impacto sobre quem fez a chamada;

# Argumentos e referências compartilhadas 
def changer(x, y): # função 
    x = 2          # altera apenas o valor do nome local 
    y[0] = 'spam'  # altera o objeto compartilhado no local 

x = 1 
L = [1, 2]    # quem faz a chamada 
changer(x, L) # passa imutável e mutável 
print (x)     # x inalterado = 1 
print (L)     # L é diferente = ['spam', 2]

# Evitando alterações de argumento mutável
L = [1, 2]
changer(x, L[:]) # passa uma cópia; portanto, meu L não muda

def changer(x, y):
    y = y[:]      # copia a lista de entrada; portanto, não afeta quem fez chamada 
    x = 2 
    y[0] = 'spam' # altera apenas a cópia de minha lista

# Simulando parâmetros de saída 
def multiple(x, y):
    x = 2 
    y = [3, 4]
    return x, y 

x = 1 
L = [1, 2]
x, L = multiple(x, L) 
print (x) # 2
print (L) # [3, 4]

# continua ...













