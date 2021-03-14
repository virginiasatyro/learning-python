# A INSTRUÇÃO CLASS
# CLASS é uma construtora de objetos e uma atribuição implícita;

# Forma geral
'''
class <nome> (superclasse, ...):  # atribui ao nome 
	data = valor                  # dados de classe compartilhados 
	def metodo(self...):          # métodos 
		self.membro = valor       # dados por instância
'''

# Exemplo
class ShareData:
	spam = 42  # gera atributo de classe 
	
x = ShareData()  # produz duas instâncias 
y = ShareData()
print(x.spam)  # = 42 
print(y.spam)

ShareData.spam = 99 
print(x.spam)          # 99 
print(y.spam)          # 99 
print(ShareData.spam)  # 99 

x.spam = 88 
print(x.spam)          # 88
print(y.spam)          # 99 
print(ShareData.spam)  # 99 

class MixeNames:                # define a classe 
	data = 'spam'               # atribui atributo de classe 
	def __init__(self, value):  # atribui nome de método 
		self.data = value       # atribui atributo de instância
	def display(self):
		print(self.data)        # atributo de instância
		print(MixeNames.data)   # atributo e classe 
		
x = MixeNames(1) # produz dois objetos instância
y = MixeNames(2) # cada um tem seus próprios dados 
x.display()      # 1 spam 
y.display()      # 2 spam 


# MÉTODOS
# O SELF do Python é semelhando ao THIS do C++

# Exemplo 
class NextClass:             # define a classe 
	def printer(self, text):  # define o método 
		self.message = text      # altera a instância
		print(self.message)      # altera a instância

x = NextClass() # produz instância

''' 
--------------------------------------------------------------------
HIDDEN PAGRE

PAG 323 2 324
--------------------------------------------------------------------
'''

# Especializando métodos herdados 
class Super:
	def method(self):
		print('in Super.method')

class Sub(Super):
	def method(self):                  # anula method
		print ('starting Sub.method')  # adicionar ações aqui 
		Super.method(self)             # executa a ação padrão 
		print ('ending Sub.method')

x = Super()  # cria uma instância de Super 
x.method()   # executa Super.method = 'in Super.method'

x = Sub()   # cria uma instância de sub
x.method()  # executa Sub.method, que chama Super.method (imprime 3 frases)

# Técnicas de interface de classe
class Super:
	def method(self):
		print('in Super.method')  # comportamento padrão 
	def delegate(self):
		self.action()             # esperado para ser definido 

class Inheritor(Super):  # substitui o método completamente
	pass 
	
class Replacer(Super):  # substitui o método completamente
	def method(self):
		print('in Replacer.method')

class Extender(Super):
	def method(self):
		print('starting Extender.method')
		Super.method(self)
		print('ending Extender.method')
	
class Provider(Super):
	def action(self):
		print('in Provider.action')
		
if __name__ == '__main__':
	for klass in (Inheritor, Replacer, Extender):
		print('\n' + klass.__name__ + '...')
		klass().method()
	print('\nProvider...')
	x = Provider()
	x.delegate()
	
'''
Inheritor...
in Super.method

Replacer...
in Replacer.method

Extender...
starting Extender.method
in Super.method
ending Extender.method

Provider...
in Provider.action
'''

# Seperclasses abstratas
'''
Preencher espaços em branco é típico dos modelos de POO. Por exemplo, a 
classe pode esperar para que partes de seu comportamento sejam fornecidas
pelas subclasses.
'''
class Super:
	def method(self):
		print('in Super.method')
	def delegate(self):
		print(self.action())
	def action(self):
		assert 0, 'action must be defined!'

# ASSERT - se essa expressão for avaliada como falsa, lançará uma exceção com uma 
# mensagem de erro.

''' 
--------------------------------------------------------------------
HIDDEN PAGRE

PAG 328
--------------------------------------------------------------------
'''

'''
MÉTODO               SOBRECARGA                      CHAMADO POR
__repr__, __str__    impressão, conversões           print(x), print('x'), str(x)
__call__             chamadas de função              x{}
__getattr__          qualificação                    x.undefined 
__setattr__          atribuição de atributo          x.any = value 
__getitem__          indexação                       x[key], loops for, testes in 
__setitem__          atribuição de índice            x[key], testes de verdade 
__len__              comprimento                     len(x), testes de verdade
__cmp__              comparação                      x == y, x < y 
__lt__               comparação específica           x < y (ou então __cmp__)
__eq__               comparação específica           x == y (ou então __cmp__)
__radd__             operador '+' no lado direito    não-instância + X
__iadd__             adição no local (ampliada)      x += y (ou então __add__)
__iter__             contextos de iteração           loops for, testes in, outros
'''
# Todos os métodos de sobrecarga têm nomes que começam e terminam com "__";

# __getitem__ Intercepta Referências de Índice
class indexer:
	def __getitem__(self, index):
		return index ** 2

x = indexer()
print(x[2]) # x[i] chama __getitem__(x, i) = 4 
for i in range(5):
	print(x[i]) # 0 1 4 9 16 

#__getitem__ e __iter__ Implementam Iteração
class stepper:
	def __getitem__(self, i):
		return self.data[i]
	
x = stepper()  # x é um objeto stepper
x.data = "spam"

print(x[1])     # = 'p'
for item in x:  # loops dor chamam __getitem__
	print(item) # para itens de índices 0..N = s p a m

print('p' in x)        # = True
print([c for c in x])  # abrangência de lista = ['s', 'p', 'a', 'm']
print(map(None, x))
(a, b, c, d) = x       # atribuição de sequência
print(a + b + c)       # = spa
print(list(x))         # = ['s', 'p', 'a', 'm']
print(tuple(x))        # =('s', 'p', 'a', 'm')
print(''.join(x))      # spam 

# Iteradores Definidos Pelo Usuário
class Squares:
	def __init__(self, start, stop):
		self.value = start - 1 
		self.stop = stop
	def __iter__(self): # obtém objeto iterador 
		return self 
	def next(self):
		if self.value == self.stop:
			raise StopIteration 
		self.value += 1 
		return self.value ** 2 
'''
from iters import Squares
for i in Squares(1, 5):
	print(x)
!!!! ImportError: No module named 'iters'
'''

# __getattr__ e __setattr__ Capturam Referências de Atributo
# __getattr__ intercepta qualificações de atributo.
class empty:
	def __getattr__(self, attrname):
		if attrname == "age":
			return 40 
		else:
			# raise AttributeError, attrname
			return 0
			
x = empty()
print(x.age)  # = 40

# __setattr__ intercepta todas as atribuições de atributo.
class accesscontrol:
	def __setattr__(self, attr, value):
		if attr == 'age':
			self.__dict__[attr] = value
		else:
			return 0
			# raise AttributeError, attr + ' not allowed'

x = accesscontrol()
x.age = 40
print(x.age) # = 40 

# __repr__ e __str__ Retornam Representações de String
class adder:
	def __init__(self, value = 0):
		self.data = value   # inicializa dados 
	def __data__(self, other):
		self.data += other  # adiciona outros no local 
		
class addrepr(adder):                     # herda __init__, __add__
	def __repr__(self):                   # adiciona representação de string 
		return 'addrepr(%s)' % self.data  # converte para string como código 

x = addrepr(2)  # executa __init__
'''
x + 1           # executa __add__ 
!!!Aparentemente não funciona em Python 3!!!
'''

class addstr(adder):
	def __str__(self):                    # __str___, mas não __repr__
		return '[Vaçue: %s]' % self.data  # converte para string amigável

x = addstr(3)
'''
x + 1 
print(x)
!!!Aparentemente não funciona em Python 3!!!
'''

'''
Aparentemente algumas coisas desse capítulo não funcionam em Python 3,
sendo assim, pularei os proximos conteúdos.
'''