# OCULTAÇÃO DE DADOS EM MÓDULOS
# No Python, a ocultação de dados em módulos é uma convenção e não uma restrição
# sintática;
# Encapsulamento no Python - tem mais relação com o empacotamento do que com res];

# Minimizando o Dado de from*: _X e __all__
# Prefixar nomes com um único _ evita que eles sejam copiados quando um cliente 
# importa com uma instrução from*;


# ATIVANDO FUTUROS RECURSOS DA LINGUAGEM
# as mudanças n linguagem que possivelmente podem arruinar código já existente no 
# futuro são introduzidas gradualmente;
# from __future__ import nomedorecurso 


# MODOS DE UTILIZAÇÃO MISTOS: __name__ E __main__
# códigos de autoteste...


# ALTERANDO O CAMINHO DE PESQUISA DE MÓDULO


# A INTRUÇAO IMPORT COMO EXTENSÃO
'''
import longmodulename as name
OU 
import longmodulename
name = longmodulename
del longmodulename
OU 
from module import longname as name
'''


# CONCEITOS DE DESIGN DE MÓDULOS
''' 
* Você está sempre em um módulo no Python;
* Minimize o acoplamento de módulo: variáveis globais;
* Maximize a coesão de módulo: objetivo unificado;
* Raramente os módulos devem alterar variáveis de outros módulos;
'''
'''
MÓDULOS
	Variáveis 
	
	Funções
		Variáveis
		
	Classes
		Membros
			Métodos
'''

# Os Módulos São Objetos: Meta-programas
# um móulo que lista os espaços de nome de outros módulos
''' mydir.py
verbose = 1
def listing(module):
	if verbose:
		print("-"*30)
		print("name: ", module.__name__, " file: ", module.__file__)
		print("-"*30)
	
	count = 0
	for attr in module.__dict__.keys():  # percorre o espaço de nome 
		print("%02d) %s" % (count, attr))
		if attr[0:2] == "--":
			print("<built-in name>")     # pula __file__ etc. 
		else:
			print(getattr(module, attr)) # o mesmo que .__dict__[attr]
		count = count + 1 
		
	if verbose:
		print("-"*30)
		print(module.__name__, "has %d names" % count)
		print("-"*30)
		
	if __name__ == "__main__":
	import mydir 
	listing(mydir) # código de auto-teste: lista myself
'''


# PROBLEMAS DOS MÓDULOS
# Importando Módulos Pela String de Nome 
'''
modname = "string"
exec "import " + modname  # executa uma string de código
string                    # importada neste espaço de nome 
OU 
modname = "string"
string = __import__(modname)
string 
'''

# A Instrução From Copia Nomes, Mas Não Vincula

# A Ordem da Instrução É Importante no Código de Nível Superior

# Importações "From" Recursivas Podem Não Funcionar

# A Função Reload Pode Não Ter Impacto Nas Importações Com From

# Reload, From e Testes Interativos 

# Reload Não É Aplicado Transitivamente

'''
Esse caítulo apresentou detalhes teóricos demais, por isso li rapidamente;
'''