# Arquivos e paths de arquivo
'''
x 
''' 
# Barra invertida no Windows e barra para frente no OS X e no Linux
'''
No Windows, os paths são escritos com barras invertidas (\) como separador
entre os nomes das pastas. No OS X e no Linux, porém, utilize a barra para
frente (/) como separador de path. Se quiser que seus programas funcionem
em todos os sistemas operacionais, seus scripts Python deverão ser escritos
para tratar ambos os casos.
Felizmente, isso é simples de fazer com a função os.path.join(). Se você lhe
passar os valores de string com os nomes individuais dos arquivos e das
pastas de seu path, os.path.join() retornará uma string com um path de arquivo
que utilizará os separadores corretos de path. Digite o seguinte no shell
interativo:
'''
import os
os.path.join('usr', 'bin', 'spam') # 'usr\\bin\\spam'
# a chamada no OS X ou no Linux, a string seria 'usr/bin/spam'.

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('C:\\Users\\asweigart', filename))
# C:\Users\asweigart\accounts.txt
# C:\Users\asweigart\details.csv
# C:\Users\asweigart\invite.docx

# Diretório de trabalho atual
import os
print(os.getcwd()) # C:\GitHub\Learning_Python\Automatize Tarefas\PARTE II - Automatizando Tarefas\CAP 8 - Lendo Escrevendo Arquivos
'''
os.chdir('C:\\Windows\\System32')     -> altera diretório de trabalho
os.getcwd() # 'C:\\Windows\\System32  -> obtem diretório
'''

# Comparação entre paths absolutos e relativos
'''
Há duas maneiras de especificar um path de arquivo.
• Um path absoluto, que sempre começa com a pasta-raiz.
• Um path relativo, que é relativo ao diretório de trabalho atual do programa.
'''

# Criando novas pastas com os.makedirs()
'''
Seus programas podem criar novas pastas (diretórios) com a função
os.makedirs(). Digite o seguinte no shell interativo:
'''
import os
# os.makedirs('C:\\delicious\\walnut\\waffles') -> cria diretório

# Módulo os.path
# Lidando com paths absolutos e relativos
'''
O módulo os.path disponibiliza funções que retornam o path absoluto de um
path relativo e para verificar se um dado path representa um path absoluto.
• Chamar os.path.abspath(path) retornará uma string com o path absoluto
referente ao argumento. Essa é uma maneira fácil de converter um path
relativo em um path absoluto.
• Chamar os.path.isabs(path) retornará True se o argumento for um path
absoluto e False se for um path relativo.
• Chamar os.path.relpath(path, início) retornará uma string contendo um path
relativo ao path início para path. Se início não for especificado, o diretório de
trabalho atual será usado como path de início.
'''
print(os.path.abspath('.'))          # C:\GitHub\Learning_Python\Automatize Tarefas\PARTE II - Automatizando Tarefas\CAP 8 - Lendo Escrevendo Arquivos
print(os.path.abspath('.\\Scripts')) # C:\GitHub\Learning_Python\Automatize Tarefas\PARTE II - Automatizando Tarefas\CAP 8 - Lendo Escrevendo Arquivos\Scripts
os.path.isabs('.') # False
os.path.isabs(os.path.abspath('.')) # True

print(os.path.relpath('C:\\Windows', 'C:\\')) # Windows
# 'Windows'
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')) # ..\..\Windows
# '..\\..\\Windows'
print(os.getcwd()) # C:\GitHub\Learning_Python\Automatize Tarefas\PARTE II - Automatizando Tarefas\CAP 8 - Lendo Escrevendo Arquivos
# 'C:\\Python34'

path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path) # 'calc.exe'
os.path.dirname(path)  # 'C:\\Windows\\System32'

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath) # ('C:\\Windows\\System32', 'calc.exe')

(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
# ('C:\\Windows\\System32', 'calc.exe')

calcFilePath.split(os.path.sep) # ['C:', 'Windows', 'System32', 'calc.exe']
'/usr/bin'.split(os.path.sep)   # ['', 'usr', 'bin']

# Obtendo os tamanhos dos arquivos e o conteúdo das pastas
'''
Após ter dominado as maneiras de lidar com paths de arquivo, você poderá
começar a reunir informações sobre arquivos e pastas específicos. O módulo
os.path disponibiliza funções para obter o tamanho de um arquivo em bytes e
os arquivos e as pastas que estiverem em uma determinada pasta.
• Chamar os.path.getsize(path) retornará o tamanho em bytes do arquivo no
argumento path.
• Chamar os.listdir(path) retornará uma lista de strings com nomes de arquivo
para cada arquivo no argumento path. (Observe que essa função está no
módulo os, e não em os.path.)
'''

os.path.getsize('C:\\Windows\\System32\\calc.exe') # 776192 (bytes)
os.listdir('C:\\Windows\\System32') # ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
# 'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

'''
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
	totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize) # 1117846456 (bytes)
'''

# Verificando a validade de um path
'''
• Chamar os.path.exists(path) retornará True se o arquivo ou a pasta
referenciada no argumento existir e retornará False caso contrário.
• Chamar os.path.isfile(path) retornará True se o argumento referente ao path
existir e for um arquivo e retornará False caso contrário.
• Chamar os.path.isdir(path) retornará True se o argumento referente ao path
existir e for uma pasta e retornará False caso contrário.
'''

print(os.path.exists('C:\\Windows'))                     # True
print(os.path.exists('C:\\some_made_up_folder'))         # False
print(os.path.isdir('C:\\Windows\\System32'))            # True
print(os.path.isfile('C:\\Windows\\System32'))           # False
print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))  # False
print(os.path.isfile('C:\\Windows\\System32\\calc.exe')) # True

print(os.path.exists('D:\\')) # True - tem um DVD ou pen drive 

# Processo de leitura/escrita




