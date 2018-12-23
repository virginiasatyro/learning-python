# CATEGORIAS DE TIPO REVISTAS
'''
TIPOS DE OBJETO  CATEGORIA  MUTÁVEL?
Númetos          Numérico   Não
Strings          Sequência  Não
Listas           Sequência  Sim
Dicionários      Mapeamento Sim
Tupla            Sequência  Não
Arquivos         Extensão   n/a
'''


# GERENALIDADE DE OBJETO
'''
* Listas, dicionários e tuplas podem conter qualquer tipo de objeto;
* Listas, dicionários e tuplas podem ser aninhados arbitrariamente;
* Listas e dicionários podem aumentar e diminuir dinamicamente;
'''

# Árvore de objetos sequência compostos aninhados:
L = ['abc', [(1, 2), ([3], 4)], 5]
L[1]          # [(1, 2), ([3], 4)]
L[1][1]       # ([3], 4)
L[1][1][0]    # [3]
L[1][1][0][0] # 3


# REFERÊNCIAS VERSUS CÓPIAS
X = [1, 2, 3]
L = ['a', X, 'b'] # incorpora referências para o objeto de x
D = {'x': X, 'y': 2}
# como listas são mutáveis, alterar o objeto lista compartilhada, a partir de
# qualquer uma das três referências, altera o que as outras duas referenciam:
X[1] = 'surprise' # altera todas as 3 referências!!!
L # ['a', [1, 'surprise', 3], 'b']
D # {'x': [1, 'surprise', 3], 'y': 2}

# Referências são um analogia de npivel mais alto aos ponteiros de outras linguagens;
'''
Se quisermos cópias, devemos solicitá-las:
* Expressões de fracionamento com limites vazios copiam sequências;
* O método de dicionário copu copia um dicionário;
* Algumas funções internas, como list, também fazem cópias;
* O módulo de biblioteca padrão copy faz cópias completas;
'''

L = [1, 2, 3]
D = {'a': 1, 'b': 2}
# atribuir cópias a outras variáveis e não referências
A[1] = L[:]  # em vez de: A = L (list(L))
B = D.copy() # em vez de B = D
# alterações nas cópias, não nos originais
A[1] = 'Ni'
B['c'] = 'spam'
L, D # ([1, 2, 3], {'a': 1, 'b': 2})
A, B # ([1, 'Ni', 3], {'a': 1, 'c': 'spam', 'b': 2})

X = [1, 2, 3]
L = ['a', X[:], 'b'] # incorpora cópias do objeto
D = {'x': X[:], 'y': 2}


# COMPARAÇÕES, IGUALDADE E VERDADE
# Todos os objetos do Python respondem às comparações.
L1 = [1, ('a', 3)] # o mesmo valor, objetos exclusivos
L2 = [1, ('a', 3)]
L1 == L2, L1 is L2 # equivalente? o mesmo objeto? = (1, 0)
# o operador == testa equivalência de valor
# o operador IS testa a identidade do objeto - mesmo objeto? mesmo endereço de memória?

S1 = 'spam'
S2 = 'spam'
S1 == S2, S1 is S2 # (1, 1) - acontece com strings curtas em Python - guardadas na cache

S1 = 'a longer string'
S2 = 'a longer string' 
S1 == S2, S1 is S2 # (1, 0)

L1 = [1, ('a', 3)] 
L2 = [1, ('a', 2)]
L1 < L2, L1 == L2, L1 > L2 # tupla de resultados = (0, 0, 1)

# exemplos de valores verdadeiros e falsos de objetos
'''
OBJETO  VALOR
"spam"  Verdadeiro
""      Falso
[]      Falso
{}      Falso
1       Verdadeiro
0.0     Falso
None    Falso
'''

# None - lugar reservado vazio - pareciso com NULL em C;
L = [None] * 100 # alocando uma lista com 100 objetos none
L # [None, None, None,...]


# HIERARQUIA DE TIPO DO PYTHON
'''
NÚMEROS -> Inteiros -> Inteiro Longo Booleano
        -> Ponto flutuante Complexo

COLEÇÕES -> Sequências -> Imutáveis -> String Unicode Tupla
                       -> Mutáveis  -> Listas
		 -> Mapeamento -> Dicionário
		 
PODEM SER CHAMADAS -> Funções Classe Método -> Vinculado
											-> Não vinculado

OUTROS -> Módulo Instância Arquivo None

FUNCIONAMENTO INTERNO -> Tipo Código Quadro Rastreamento
'''

# PROBLEMAS DOS TIPOS INTERNOS 
# * A atribuição cria referências e não cópias;
# * A repetição acrescenta um nível de profundidade;
L = [4, 5, 6]
X = L * 4   # [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
Y = [L] * 4 # [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]
# * Estruturas de dados cíclicas;
L = ['grail'] # anexa referência para mesmo objeto
L.append(L)   # gera ciclo no objeto: [...] (loop inesperado)
L             # ['grail', [...]]
# * Tipos imutáveis não podem ser alterados no local;
T = [1, 2, 3] 
T[1] = 4 # Erro!
T = T[:2] + (4,) # Tudo bem = (1, 2, 4) ---> constrói novo objeto com fracionamento, concatenação, ...
# essa linha não funciona em Python 3