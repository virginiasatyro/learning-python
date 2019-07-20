#----------------------------------
# fazer ajustes
# ---------------------------------






# AS CLASSES GERAM VÁRIOS OBJETOS INSTÂNCIA
'''
* No Pyhton, existem dois tipos de objetos - objetos de classe e de 
instância;
'''
# Os Objetos Classe Fornecem Comportamento Padrão
'''
* A instrução CLASS cria um objeto classe e atribui um nome a ele;
* As atribuições dentro de instruções CLASS produzem atributos de 
classe;
* Os atributos da classe fornecem o estado e o comportamento do objeto;
'''

# Os Objetos Instância são Itens Concretos
'''
* Chamar um objeto classe como uma função produz um novo objeto 
instância;
* Cada objeto instância herda atributos da classe e recebe seu próprio
espaço de nome;
* As atribuições aos atributos de SELF em métodos produzem atributos 
por instância;
'''

class FirstClass:              # define um objeto classe 
	def setdata(self, value):  # define métodos de classe
		self.data = value      # self é a instância 
	def display(self): 
		print (self.data)      # self.data: por intância
		
x = FirstClass() # produz duas instâncias
y = FirstClass() # cada uma é um novo espaço de nome

x.setdata("King Arthur")  # chama métodos: self é x 
y.setdata(3.141559)       # executa: FirstClass.setdata(y, 3.141559)

x.display() # King Arthur
y.display() # 3.141559

x.data = "New value"
x.display() # New value


# AS CLASSES SÃO PERSONALIZADAS POR MEIO DE HERANÇA
'''
* As superclasses são listadas entre parênteses no cabeçalho de uma 
instrução class;
* 
////////////////////////////////////////////////

HIDDEN PAGE?????????????????????????????????????? (pdf)
pagina 314
////////////////////////////////////////////////
'''

# Classes e módulos
# Poderíamos importar e usar a classe:
'''
from modulename import.FirstClass # copia o nome em meu escopo
class SecondClass(FirstClass):    # usa o nome da classe diretamente
	def display(self): ...
	
OU

import modulename                          # acessa o módulo inteiro
class SecondClass(modulename, FirstClass): # qualifica para referenciar
	def display(self): ...
'''

# Arquivo food.py
'''
var = 1      # food.var 
def func():  # food.func
...
class spam:  # food.spam 
...
class ham:   # food.ham 
...
class eggs:  # food.eggs
...
'''

# Arquivo person.py 
'''
class person:
...

import person        # importa módulo
x = person.person()  # classe dentro do módulo 

OU 

from person import person  # obtém a classe a partir do módulo 
x = person()               # usa o nome da classe 
'''


# CLASSES PODEM INTERCEPTAR OPERADORE DO PYTHON
# A sobrecarga de operadores permmite que objetos desenvolvidos com classes interceptem
# e respondam às operações que funicionam em tipos internos: adição, impressão, etc.
'''
* Os métodos com nomes como __x__ são ganchos especiais;
* Tais métodos são chamados automaticamente quando o Python avalia operadores;
* As classes podem anular a maioria das operações de tipo inteiro;
* Os operadores permitem que as classes sejam integradas com o modelo de objeto 
do Python;
'''

'''
class ThirdClass(SecondClass):                # é um SecondClass
	def __init__(self, value):                # em ThirdClass(value)
		self.data = value
	def __add__(self, other):                 # em "self + other"
		return ThirdClass(self.data + other)
	def __mul__(self, other):
		self.data = self.data * other         # em "self * other"
	
a = ThirdClass("abc")  # novo __init__ chamado 
a.display()            # método herdado  "abc"

b = a + 'xyz' # novo __add__: cria uma nova instância
b.display()   # = abcxyz 

a * 3        # novo __mul__: altera instância no local 
a.display()  # = abcabcabc
a.display()
'''