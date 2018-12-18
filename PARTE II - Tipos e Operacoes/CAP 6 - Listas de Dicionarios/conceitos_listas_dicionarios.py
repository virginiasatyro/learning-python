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








