# ARQUIVOS

'''
OPERAÇÃO INTERPRETAÇÃO
output = open('/tmp/spam', 'w') Cria arquivo de saída ('w' significa gravação)
input = open('data', 'r')       Cria arquivo de entrada ('r' significa leitura)
S = input.read()                Lê o arquivo inteiro em uma única string
S = input.read(N)               Lê N bytes (1 ou mais)
S = input.readline()            Lê a próxima linha (até o marcador de final de linha)
L = input.readlines()           Lê o arquivo inteiro na lista de strings da linha
output.write(S)                 Grava a string S no arquivo
output.writelines(L)            Grava no arquivo todas as strings da linha da lista
output.close()                  Fechamento manual 
'''

myfile = open('myfile', 'w')      # abre para saída (cria)
myfile.write('hello text file\n') # grava uma linha de texto
myfile.close()

myfile = open('myfile', 'r') # abre para entrada
myfile.readline()            # lê a linha de volta = 'hello text file\n'
myfile.readline()            # string vazia: fim do arquivo