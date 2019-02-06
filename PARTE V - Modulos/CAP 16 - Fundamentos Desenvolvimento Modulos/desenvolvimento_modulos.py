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
# * IMPORT - atribui a um objeto módulo inteiro a um único nome;
# * FROM - atribui um ou mais nomes a objetos de mesmo nome em outro módulo;
from small import x, y # copia 2 nomes
print(x)    # 1 
print(y[0]) # 1 
x = 42
print(x)    # 42 
print(y[0]) # seria 42 em versões anteriores do Python, para a versão 3, permanece 1
''' 
Aparentemente algumas regras do capítulo não se aplicam a Python 3,
pularei alguns exemplos.
'''

import small
print(small.y) # [1, 2]

'''
from module import name1, name2    # copia esses dois nomes (apenas)

import module           # busca o objeto módulo
name1 = module.name1    # copia nomes pela atribuição
name2 = module.name2
del module              # desfaz-se do nome do módulo
'''


# ESPAÇOS DE NOME DE MÓDULO



