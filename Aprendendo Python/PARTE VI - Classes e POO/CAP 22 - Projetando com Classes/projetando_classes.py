# PYTHON E POO 
'''
HERANÇA
- é baseada em pesquisa de atributos no Python (em expressões x.nome);
POLIMORFISMO
- em x.metodo, o significado de método depende do tipo (classe) de x;
ENCAPSULAMENTO
- os métodos e os operadores implementam comportamento; a ocultação de 
dados é uma convenção, por padrão;
'''

# Sobrecarga Por Assinaturas de Chamada (ou não)
class C:
	def meth(self, x):
		x.operation()  # presume que x faz a coisa certa
		
		
# CLASSE COMO REGISTROS
rec = {}
rec['name'] = 'mel'
rec['age'] = 40
rec['job'] = 'trainer/writer'

print(rec['name'])  # mel 

# fazendo isso por meio de classes
# esse código tem significativamente menos sintaxe do que o equivalente com dicionário
class rec: pass # instrução class vazia para gerar um objeto espaço de nome vazio
rec.name = 'mel'
rec.age = 42
rec.job = 'trainer/writer'

print(rec.age) # 42


class rec: pass 
# dois registros a partir da mesma classe 
pers1 = rec();
pers1.name = 'mel'
pers1.job = 'trainer'
pers1.age = 40

pers2 = rec()
pers2.name = 'dave'
pers2.job = 'developer'

print(pers1.name) # mel 
print(pers2.name) # dave 


class Person:
	def __init__(self, name, job):
		self.name = name
		self.job  = job 
	def info(self):
		return (self.name, self.job)
		
mark = Person('ml', 'trainer')
dave = Person('da', 'developer')
 
print(mark.job)    # trainer
print(dave.info()) # ('da', 'developer') 


# POO E HERANÇA: RELACIONAMENTOS "É UM"

# Hidden page - verificar o que está escrito no livro impresso!

# POO E DELEGAÇÃO
# Delegação normalmente implica em objetos controladores que incorporam outros objetos,
# para os quais passam pedidos de operação. Gancho de método: __getattr__

class wrapper:
	def __init__(self, object):
		self.wrapped = object                  # salva o objeto
	def __getattr__(self, attrname):
		print('Trace: ' + attrname)            # busca de Trace
		return getattr(self.wrapped, attrname) # busca do delegado

x = wrapper([1, 2, 3]) 
x.append(4)      # Trace: append
print(x.wrapped) # [1, 2, 3, 4]

x = wrapper({"a": 1, "b": 2})
x.keys()         # Trace: keys
print(x.wrapped) # {'b': 2, 'a': 1}


# HERANÇA MÚLTIPLA
'''
Na instrução class,mais de uma superrclasse pode ser listada entre parênteses na
linha de cabeçalho. Quando faz isso, você utiliza a herança múltipla - a classe 
e suas instâncias herdam nomes de todas as superclasses listadas.
'''

# Hidden page - verificar o que está escrito no livro impresso!
'''
from mytools import Lister # obtem classe de ferramenta

class Super:
	def __init__(self): # __init__ da superclasse 
		self.data1 = "spam"

class Sub(Super, Lister): # mistura um __repr__
	def __init__(self): # Lister tem acesso a self 
		Super.__init__(self)
		self.data2 = "eggs"  # mais atributos de instância 
		self.data3 = 42 

X = Sub()
print(X)
'''

# Hidden page - verificar o que está escrito no livro impresso!

# CLASSES VERSUS MÓDULOS
'''
MÓDULOS
	* são pacotes de dados/lógica
	* são criados escrevendo-se arquivos em Python ou extensões em C
	* são usados por meio de importação
CLASSES
	* implementam novos objetos
	* são criadas por meio de instruções class
	* são usadas por meio de chamadas
	* sempre residem dentro de um módulo
'''



















