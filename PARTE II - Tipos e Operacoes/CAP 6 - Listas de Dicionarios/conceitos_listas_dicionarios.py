# LISTAS
# Tipo de objeto coleção ordenada flexível do Python.
# Propriedades principais:
#     Coleções ordenadas de objetos arbitrários;
#     Acessadas pelo deslocamento;
#     Têm comprimento variável, são heterogêneas e podem ser aninhadas arbitrariamente;
#     Categoria sequência mutável;
#     Arrays de referência de objeto;

'''
OPERAÇÕES COMUNS DE LISTAS
OPERAÇÃO                      INTERPRETAÇÃO
L1 = []                       Uma lista vazia
L2 = [0, 1, 2]                Três itens: índices 0..2
L3 = ['abc', ['def', 'ghi']   Sublistas aninhadas
L2[i]                         Índice
L3[i][j]                      Índice de índice
L2[i:j]                       Fracionamento
len(L2)                       Comprimento
L1 + L2                       Concatenação
L2 * 3                        Repetição
for x in L2                   Participação como membro
L2.append(4)                  Métodos: grow, sort, search, reserve, etc.
L2.extend([5, 6, 7])
L2.sort()
L2.index(1)
L2.reverse()
del L2[k]                     Redução
del L2[i:j]
L2[i] = 1                     Atribuição de índice
L2[i:j] = [4, 5, 6]           Atribuição de fracionamento
range(4)                      Produz listas/tuplas de inteiros
xrange(0, 4)
L4 = [x**2 for x in range(5)] Abrangência de lista
'''

# OPERAÇÕES DE LISTAS BÁSICAS
len([1, 2, 3])              # Comprimento = 3
[1, 2, 3] + [4, 5, 6]       # Concatenação = [1, 2, 3, 4, 5, 6]
['Ni!'] * 4                 # Repetição = ['Ni!','Ni!', 'Ni!', 'Ni!']
3 in [1, 2, 3]              # Participação como membro = 1 (significa TRUE)
for x in [1, 2, 3]: print x # Iteração = 1 2 3 

'[1, 2]' + "34"     # '[1, 2]34'
[1, 2] + list("34") # [1, 2, '3', '4']

# INDEXAÇÃO, FRACIONAMENTO E MATRIZES
L = ['spam', 'Spam', 'SPAM'] 
L[2]  # 'SPAM'    Os deslocamentos começam do zero
L[-2] # 'Spam'    Negativo: conta a partir da direita
L[1:] # ['Spam', 'SPAM']

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # array bidimensional 3 x 3 
matrix[1]    # [4, 5, 6]
matrix[1][1] # 5
matrix[2][0] # 7
matrix[[1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]]
matrix[1][1] # 5
# NumPy - fornece também outras maneiras de manipular matrizes

# Atribuição de índice e fracionamento
L = ['spam', 'Spam', 'SPAM']
L[1] = 'eggs' # Atribuição de índice
L # ['spam', 'eggs', 'SPAM']
L[0:2] = ['eat', 'more'] # Atribuição de fracionamento: exclusão + inserção
L # ['eat', 'more', 'SPAM']

# Chamadas de métodos de lista
L.append('please') # anexa chamada de método
L # ['eat', 'more', 'SPAM', 'please']
L.sort() # ordena os itens da lista ('S' < 'e')
L # ['SPAM', 'eat', 'more', 'please']

L = [1, 2]
L.extend([3, 4, 5]) # anexa vários itens
L # [1, 2, 3, 4, 5]
L.pop() # exclui, retorna o último item - retorna: 5
L # [1, 2, 3, 4]
L.reverse() # inversão no local
L # [4, 3, 2, 1]

L = []
L.append(1) # coloca na pilha
L.append(2)
L # [1, 2]
L.pop() # retira da pilha - retorna 2
L # [1]

L # ['SPAM', 'eat', 'more', 'please']
del L[0] # exclui um item
L # ['eat', 'more', 'please']
del L[1:] # exclui uma seção inteira
L # ['eat']

L = ['Already', 'got', 'one']
L[1:] = []
L # ['Already']
L[0] = []
L # [[]]


# DICIONÁRIOS
# Dicionários são coleções desordenadas;
# Os ítens são armazenados e buscados pela chave, em vez de deslocamento posicional;
# Podem substituir muitos dos algoritmos de pesquisa e estrutura de dados;
# Principais propriedades:
#    Acessados pela chave e não pelo deslocamento - arrays associativos/tabela de hashing
#    Coleções desordenadas de objetos arbitrários; - chave simbólica, e não física
#    Têm comprimento variável, são heterogêneos e podem ser aninhados arbitrariamente;
#    Categoria mutável mapeamento;
#    Tabelas de referências de objetos (tabelas de hashing);

# DICIONÁRIOS EM AÇÃO

'''
OPERAÇÃO INTERPRETAÇÃO
D1 = {}                              Dicionário vazio
D2 = {'spam': 2, 'eggs': 3}          Dicionário de dois itens
D3 = {'food': {'ham': 1, 'eggs': 2}  Aninhamento
D2['eggs']                           Indexação pela chave
D3['food']['ham']
D2.has_key('eggs'), 'eggs' in D2     Métodos: teste de participação como membro,
D2.keys()                            listas de chaves, lista de valores, cópias, padrões, intercalação, etc.
D2.values()
D2.copy()
D2.get(key, default)
D2.update(D1)
len(D1)                              Comprimento (número de entradas armazenadas)
D2[key] = 42                         Adição/alteração
del D2[key]                          Exclusão
D4 = dict(zip(keylist, valslist))    Construção (CAP 10)
'''

# Operações Básicas de Dicionário
d2 = {'spam': 2, 'ham': 1, 'eggs': 3} # faz um dicionário
d2['spam']                            # busca valor pela chave = 2
d2                                    # = {'ham': 1, 'eggs': 3, 'spam': 2} - a ordem é misturada (HASHING)

len(d2)           # número de entradas no dicionário = 3
d2.has_key('ham') # teste de participação da chave como membro (1 = true) = 1
'ham' in d2       # teste alternativo de participação da chave como membro = 1
d2.keys()         # cria uma nova lista de minhas chaves = ['eggs', 'ham', 'spam']

# Alterando dicionários no local
d2['ham'] = ['grill', 'bake', 'fry'] # altera entrada
d2                                   # {'eggs': 3, 'spam': 2, 'ham': [grill', 'bake', 'fry]}
del d2['eggs']                       # exclui entrada
d2                                   # {'spam': 2, 'ham': [grill', 'bake', 'fry]}
d2['brunch'] = 'Bacon'               # adiciona nova entrada
d2                                   # {'brunch': 'bacon', 'spam': 2, 'ham': [grill', 'bake', 'fry]}

# Mais métodos de dicionário
d2.values(), d2.items()                              # ([3, 1, 2], [('eggs', 3), ('ham', 1), ('spam', 2)])
d2.get('spam'), d2.get('toast'), d2.get('toast', 88) # (2, None, 88) - se não tiver na lista retorna NONE ou um padrão passado (88)

d2 # {'eggs': 3, 'ham': 1, 'spam': 2} 
d3 = {'toast': 4, 'muffin': 5}
d2.update(d3)
d2 # {'toast': 4, 'muffin': 5, 'eggs': 3, 'ham': 1, 'spam': 2}

# Uma Tabela de Linguagens
table = {'Python': 'Guido van Rossum',
...      'perl'  : 'Larry Wall',
...      'Tcl'   : 'John Ousterhout'}

language = 'Python'
creator  = table[language]
creator # 'Guido van Rossum'
for lang in table.keys():
...    print lang, '\t', table[lang]
...
'''
Python Guido van Rossum
Tcl    John Ousterhout
perl   Larry Wall
'''

# NOTAS SOBRE UTILIZAÇÃO DE DICIONÁRIOS
# * OPERAÇÕES DE SEQUÊNCIA NÃO FUNCIONAM: dicionários são mapeamentos e não sequenciais.
# Não há ordenação, nem fracionamento, por exemplo. 
# * ATRIBUIÇÃO A NOVOS ÍNDICES ADICIONA ENTRADAS: 
# * AS CHAVES NEM SEMPRE PRECISAM SER STRINGS:


# Usando Dicionários para Simular Listas Flexíveis
# Usando chaves inteiras, os dicionários podem simular listas que parecem crescer em atribuição de deslocamento:
D = {}
D[99] = 'spam'
D[99] # 'spam'
D     # {99: 'spam'} 

# Usando Dicionários para Estruturas de Dados Esparsas
Matrix = {}         # array tridimensional onde todas as posições são vazias exceto duas
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2; Y = 3; Z = 4 # ; separa instruções
Matrix[(X, Y, Z)]   # = 88
Matrix              # {(2, 3, 4): 88, (7, 8, 9): 99}

if Matrix.has_key((2, 3, 6)): # varifica a existência da chave antes de buscar
print Matrix[(2, 3, 6)]
else:
print 0 
# 0
try:
print Matrix[(2, 3, 6)] # tenta indexar
except keyError:
print 0
# 0
Matrix.get((2, 3, 4), 0) # existe; busca e retorna
# 88
Matrix.get((2, 3, 6), 0) # não existe; usa arg padrão
# 0

# Usando Dicionários Como "Registros"
rec = {}
rec['name'] = 'mel'
rec['age']








