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