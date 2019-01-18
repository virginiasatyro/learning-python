# CRIAÇÃO DE MÓDULOS
'''
module1.py
def printer(x): # atributo de módulo
    print(x)
'''
import module1
module1.printer(10)


# UTILIZAÇÃO DE MÓDULOS
# IMPORT - busca o módulo como um todo;
# FROM - busca nomes específicos do módulo;

# A instrução import                   
import module1                  # obtém o módulo como um todo 
module1.printer('Hello world!') # qualifica para obter nomes 

# A instrução from 
from module1 import printer
printer('Hello world!!')

# A instrução from *
from module1 import *
printer('Hello world!!!')

# As importações acontecem apenas uma vez
# Os módulos são carregados e executados na primeira instrução IMPORT ou FROM;
import simple # primeira importação: carrega e executa o código do arquivo
# = Hello 
print(simple.spam) # = 1 

# importações posteriores não executam novamente o código do módulo
simple.spam = 2    # altera atributo no módulo
import simple      # apenas busca o módulo já carregado 
print(simple.spam) # o código não foi executado novamente: atributo inalterado 
# = 2

# IMPORT e FROM são atribuições
