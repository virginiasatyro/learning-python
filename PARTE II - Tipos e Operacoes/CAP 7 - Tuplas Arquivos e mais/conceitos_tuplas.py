# TUPLAS
# Tipo de coleção;
# Contróem grupos de objetos simples;
# Funcionam como as listas, exceto que não podem ser alteradas no local;
# Escritas como uma série de itens em parênteses (não colchetes);

'''
* São coleções ordenadas de objetos arbitrários;
* São acessados pelo deslocamento;
* São da categoria sequência imutável;
* Têm comprimento fixo, são heterogêneas e podem ser aninhadas arbitrariamente;
* São arrays de referências de objeto;
'''

'''
OPERAÇÃO                    INTERPRETAÇÃO
()                          Tupla vazia
t1 = (0,)                   Tupla de um item
t2 = (0, 'Ni', 1.2, 3)      Tupla de quatro itens
t3 = ('abc', ('def', 'ghi') Tuplas aninhadas
t1[i]                       Índice
t3[i][j]                    Índice de índice
t1[i:j]                     Fracionamento
len(t1)                     Comprimento
t1 + t2                     Concatenação
t2 * 3                      Repetição
for x in t2                 Iteração
3 in t2                     Participação como membro
'''

# Tuplas não tem métodos. Ex: chamada append não funciona

(1, 2) + (3, 4)  # concatenação = (1, 2, 3, 4)
(1, 2) * 4       # Repetição = (1, 2, 1, 2, 1, 2, 1, 2)
T = (1, 2, 3, 4) # Indexação, fracionamento 
T[0], T[1:3]     # (1, (2, 3))

x = (40)   # um inteiro
x = (40, ) # uma tupla contendo um inteiro

T = ('cc', 'aa', 'dd', 'bb')
temp = list(T)
temp.sort()
temp # ['aa', 'bb', 'cc', 'dd']
T = tuple(temp)
T    # ('aa', 'bb', 'cc', 'dd')

T = (1, [2, 3], 4) # funciona
T[1][0] = 'spam' 
T                  # (1, ['spam', 3], 4)
T[1] = 'spam'      # falha