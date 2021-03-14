# FUNDAMENTOS DA IMPORTAÇÃO DE PACOTE
'''
Podemos listar um caminho de nomes separados por pontos:
import dir1.dir2.mod 
-> Caminho pela hierarquia: dir0\dir1\dir2\mod.py
-> dir0 - precisa ser adicionado ao caminho de pesquisa de módulo
OU
from dir1.dir2.mod import x 
'''

# Pacotes e configurações de caminho de pesquisa
'''
* Caminhos de diretório só podem ser variáveis separadas por pontos, ou seja,
não é possível escrever: import C:\mycode\dir1\dir2\mod;
* É preciso adicionar C:\mycode em sua variável PYTHONPATH ou arquivos pth,
a menos que ele seja o diretório de base do programa, escreva isso:
import dir1.dir2.mod 
'''

# Arquivos de pacote __init__.py 
'''
* Cada diretório nomeado dentro do caminho de uma instrução de importação de 
pacote também deve conter um arquivo chamado __init__.py, senão suas impotações
falharão;
* Para uma estrutura de diretório como:
	dir0\dir1\dir2\mod.py 
e para uma instrução de importação da forma:
	import dir1.dir2.mod 
as seguintes regras se aplicam:
- dir1 e dir2 devem ambos conter um arquivo __init__.py 
- dir0, o contêiner, não exige um arquivo __init__.py; se estiver presente, será ignorado;
- dir0 deve ser listado no caminho de pesquisa de módulo (diretório de base, PYTHONPATH etc)
e não dir0\dir1;

dir0\
	dir1\
		__init__.py
		dir2\
			__init__.py 
			mod.py 
'''

# EXEMPLO DE IMPORTAÇÃO DE PACOTE
'''
# Arquivo: dir1\__init__.py
print ('dir1 init')
x = 1 

# Arquivo: dir1\dir2\__init__.py
print ('dir2 init')
y = 2 

# Arquivo: dir1\dir2\mod.py
print ('in mod.py')
z = 3 

% python 
>>> import dir1.dir2.mod  # as primeiras impotações executam arquivos init
dir1 init
dir2 init
in mod.py 
>>> import dir1.dir2.mod  # as importações posteriores, não 
>>> reload(dir1)
dir1 init 
<module 'dir1' from 'dir1\__init__.pyc'>

>>> dir1.x 
1 
>>> dir1.dir2.y 
2 
>>> dir1.dir2.mod.z 
3
'''

# From versus import com pacotes
'''
>>> from dir1.dir2 import mod 
>>> mod.z
3 

>>> import dir1.dir2.mod import z 
>>> z 
3 

>>> import dir1.dir2.mod as mod 
>>> mod.z
3
'''