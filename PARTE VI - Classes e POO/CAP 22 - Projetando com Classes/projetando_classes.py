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

class rec: pass 
rec.name = 'mel'
rec.age = 42
rec.job = 'trainer/writer'

print(rec.age) # 42












