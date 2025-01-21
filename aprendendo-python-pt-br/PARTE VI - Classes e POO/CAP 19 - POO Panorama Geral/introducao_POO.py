# POR QUE USAR CLASSES?
'''
* HERANÇA: robôs pizzaiolos são uma espécie de robô e, assim, possuem propriedades
robóticas comuns. Eles herdam tais propriedades da categoria geral robô. Essas 
propriedades precisar ser implementadas uma vez para o caso real, e são reutilizadas
pelos robôs;

* COMPOSIÇÃO: robôs pizzaiolos são, na realidade, uma coleção de componentes que
trabalham em conjunto como uma equipe. Por exemplo, o robô precisa de braços para 
enrolar a massa, motores para manusear o forno e assim por diante. O robô é um 
exemplo de composição: contém outros objetos para cumprir as ordens. Cada 
componente pode ser definido como uma classe, definindo seu próprio comportamento
e seus relacionamentos;


- Instâncias múltiplas:
As classes são fábricas para gerar um ou mais objetos. Sempre que chamamos uma
classe, geramos um novo objeto, com nome e espaço distinto.

- Personalização por meio de herança:
As classes também suportam a noção de herança da POO. Elas são entendidas pela
redefinição de seus atributos fora da classe em si. Classes podem construir
hierarquias de espaço e de nome, as quais definem os nomes a serem usados pelos 
objetos criados a partir das classes da hierarquia.

- Sobrecarga de operador:
Fornecendo métodos de protocolo especiais, as classes podem definir objetos
que respondem às operações que vimos nos tipos internos. Por exemplo, os
objetos feitos com classes podem ser fracionados, concatenados, indexados, etc.
O Python fornece ganchos que as classes podem usar para interceptar e implementar
qualquer operação de tipo interno.
'''

# POO A 30.000 PÉS DE ALTURA
# Pesquisa de Herança de atributo:
'''
* Mais simples que implementar em C++ ou Java!
* objeto.atributo
Quando escrevemos isso para um objeto derivado de uma instrução CLASS, a 
expressão provoca uma PESQUISA no Python - ele pesquisa uma árvore de objetos
vinculados, em busca da primeira aparição do atributo que puder encontrar. 

* CLASSES: servem como fábricas de instâncias. Seus atributos fornecem 
comportamento - dados e funções - que é herdado por todas as instâncias
geradas a partir delas.

* INSTÂNCIAS: representam os itens concretos no domínio de um programa. 
Seus atributos registram dados que variam de acordo com o objeto específico.

* Superclasses e subclasses - referem-se às posições relativas na árvore e 
às funções.
'''

# Desenvolvendo Árvores de Classe 
'''
* Cada instrução CLASS gera um novo objeto classe;
* Sempre que uma classe é chamada, ela gera um novo objeto instância;
* As instâncias são vinculadas automaticamente à classe a partir da qual 
são criadas;
* As classes são vinculadas às suas subclasses, sendo listadas entre 
parênteses em uma linha de cabeçalho da instrução CLASS. A ordem da 
esquerda para a direita fornece a disposição na árvore;
'''

'''
class C2: ...         # produz objetos classe (formas ovais)
class C3: ...
class C1(C2, C3): ... # vínculos para subclasses
I1 = C1()             # produz objetos instância (retângulo)
I2 = C1()             # vinculado às suas classes 

* HERANÇA MÚLTIPLA: uma classe tem mais de uma superclasse acima dela na 
árvore.

- os atributos normalmente são anexados às classes por meio de atribuições
feitas dentro de instruções CLASS;
- os atributos são normalmente anexados às instâncias por meio de atribuições 
a um argumento especial, chamado SELF, passado para funções dentro das 
classes;

'''

class C1:                    # produz e vincula a classe C1, ex: class C1(C2, C3):
	def setname(self, who):  # atribui nome: C1.setname 
		self.name = who      # self é I1 ou I2 
I1 = C1()                    # produz duas instâncias 
I2 = C1()
I1.setname('bob')            # configura I1.name como 'bob'
I2.setname('mel')
print (I1.name)              # imprime 'bob'

# Garantindo que o atributo seja sempre configurado:
class C1:
	def __init__(self, who): # configura name quando contruído
		self.name = who      # self é I1 2 I2
I1 = C1('bob')               # configura I1.name como 'bob'
I1 = C1('mel')
# INIT - construtor

# A POO está relacionada à reutilização de código
'''
* Exemplo: banco de dados de funcionários de uma empresa
class Employee:                   # superclasse geral
	def computeSalary(self): ...  # comportamento comum ou padrão
	def giveRaise(self): ...
	def promote(self): ...
	def retire(self): ...
	
* Subclasse especializada: salário do engenheiro é calculado de outra forma;
class Engineer(Employee):       # subclasse especializada 
	def computeSalary(self):... # algo personalizado
	
bob = Employee()  # comportamento padrão
mel = Engineer()  # calculadora de salário personalizada

* Polimorfismo:
company = [bob, mel]            # um objeto composto
for emp in company:
	print(emp.computeSalary())  # executa a versão deste objeto
	
def processor(reader, converter, writer):
	while 1:
		data = reader.read()
		if not data: break 
		data = converter(data)
		writer.write(data)
		
class Reader:
	def read(self): ...      # comportamento e ferramentas padrão
	def other(self): ... 
class FileReader(Reader):
	def read(self)           # lê um arquivo local
class SocketReader(Reader): 
	def read(self): ...      # lê um soquete de rede 
	
...
processor(FileReader(...), Converter, FileWriter(...))
processor(SocketReader(...), Converter, TapeWriter(...))
processor(FtpReader(...), Converter, XmlWriter(...))
'''