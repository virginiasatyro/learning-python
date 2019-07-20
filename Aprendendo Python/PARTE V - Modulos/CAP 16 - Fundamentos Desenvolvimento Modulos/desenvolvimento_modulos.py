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
'''
No python, os módulos são ESPAÇOS DE NOME - um lugar onde nomes são criados; 
Os nomes que ficam em um módulo são chamados de seus ATRIBUTOS;
Tecnicamente, os módulos normalmente correspondem a arquivos e o Python cria um 
objeto módulo para conter todos os nomes atribuídos no arquivo, mas em termos 
simples, os módulos são apenas espaços de nome;
'''
# Arquivos geram espaços de nome 
''' 
* As instruções de módulo são executadas na primeira importação;
* As atribuições de nível superior criam atributos de módulo;
* Espaço de nome de módulo: atributo __dict__ ou dir(M);
* Os módulos são um único escopo (local é global);
'''

'''
>> imoport module2
starting to load...
done loading
'''
# Prompt de comando:
'''
>>> import module2
starting to load...
done loading
>>> module2.sys
<module 'sys' (built-in)>
>>> module2.func, module2.klass
(<function func at 0x000001AC65599B70>, <class 'module2.klass'>)
>>> module2.__dict__.keys()
dict_keys(['__file__', '__doc__', '__package__', 'klass', '__cached__', 
'__builtins__', 'sys', 'func', 'name', '__name__', '__spec__', '__loader__'])
>>> module2.__name__
'module2'
>>> module2.__file__
'C:\\GitHub\\Learning_Python\\PARTE V - Modulos\\CAP 16 - Fundamentos Desenvolvimento Modulos\\module2.py'
'''

# Qualificação de nomes de atributo
'''
* No python, você pode aceessar atributos em qualquer objeto que tenha atributos, 
usando a sintaxe de qualificação OBJETO.ATRIBUTO;
* Regras:
- Variáveis simples 
	x significa procurar o nome x nos escopos concorrentes;
- Qualificação
	x.y significa localizar x nos escopos correntes e, em seguida, procurar o
	atributo y no objeto x (não nos escopos);
- Caminhos de qualificação
	x.y.z significa pesquisar o nome y no objeto x e, em seguida, pesquisar z 
	no objeto x.y;
- Generalidade
	a qualificação funciona em todos os objetos com atributos: módulos, classs,
	tipos da linguagem C, etc;
'''

# Importações versus Escopos
''' moda.py
print('starting to load...')
import sys
name = 42 

def func(): pass
class klass: pass 

print('done loading')
'''
# -----------------------------------------------------------------
''' modb.py 
x = 11          # meu x: global apenas para esse arquivo

import moda     # obtem acesso aos nomes presentes em moda     
moda.f()        # configura moda.x e não meu x 
print (x)       # 11 
print (moda.x)  # 99
'''

# Aninhamento de espaços de nome 
''' mod3.py
x = 3
'''
# ------------------------------------------------------------------
''' mod2.py 
x = 2
import mod3

print(x)       # meu x global = 2 
print(mod3.x)  # x de mod3    = 3
'''
# ------------------------------------------------------------------
''' mod1.py 
x = 1
import mod2 # = 2 3 

print (x)            # meu x global        = 1
print (mod2.x)       # x de mod2           = 2
print (mod2.mod3.x)  # x de mod3 aninhado  = 3
'''


# RECARREGANDO MÓDULOS
'''
Por padrão, o código de um módulo é executado um vez no processo. Para obrigar
o código de um método ser recarregado e novamente executado - RELOAD;
'''

# Fundamentos de recarregamento 
'''
RELOAD - é uma função interma e não uma instrução;
RELOAD - recebe um objeto módulo existente e não um nome;

import module 
...
reload(module)
...
''' 