# ESTRUTURA DE PROGRAMA EM PYTHON
# 1. Os programas são compostos de módulos;
# 2. Os módulos contêm instruções;
# 3. As instruções contêm expressões;
# 4. As expressões cria, e processam objetos;

# * Os objetos incorporados facilitam a escrita de programas simples;
# * O Python fornece objetos e suporta extensões;
# * Os objetos incorporados são componentes de extensões;
# * Frequentemente, os objetos incorporados são mais eficientes do que as estruturas de dados personalizadas;

'''
TIPO DE OBJETO  EXEMPLO DE LITERAIS
Números         3.1415, 1234, 999L, 3 + 4j
Strings         'spam', "guido's"
Listas          {1, [2, 'three'], 4}
Dicionários     {'food' : 'spam' : 'yum'}
Tuplas          (1, 'spam', 4, 'U')
Arquivos        text = open('eggs', 'r').read()
'''

'''
LITERAL                      INTERPRETAÇÃO
1234, -24, 0                 Inteiros normais (long em C)
999999999999L                Inteiros longos (tamanho ilimitado)
1.23, 3.14e-10, 4E210        Ponto flutuante (double em C)
0177, 0x9ff, 0xFF            Literais em octal e hexadecimal
3 + 4j, 3.0 + 4.0j, 3J       Literais numéricas complexas
'''

# Operandos de expressão: +, -, >>, **etc.
# Funções matemáticas internas: pow, abs, etc.
# Módulos utilitários: random, math, etc.

# NUMPY: Numeric Python - ferramentas de programação numérica avançadas (NASA!!);

'''
OPERADORES DESCRIÇÃO
lambda args:                   expressão Geração de função anônima
x or y                         OU
x and y                        AND 
not x                          NOT
x < y, x <= y, x > y,          Operadores de comparação, igualdade, testes de identidade,
x >= y, x == y, x <> y,        e participação como membro de sequência
x != y, x is y, x is not y,
x in y, x not in y
x | y                          OU bit
x ^ y                          OU exclusivo bit
x & y                          E bit
x << y, x >> y                 Deslocamento de bits
-x + y, x - y                  Adição, subtração
x * y, x % y, x / y, x // y    Multiplicação, resto, divisão
-x, +x, ~x, x ** y             Negação, identidade, complemente bit, potência binária
x[i], x[i:j], x.attr, x(...)   Indexação, qualificação, chamadas de função
(...), [...], {...}, '...'     Tupla, lista, dicionário, conversão para string
'''

# 40 + 3.14 -> resposta é convertida para tipo numérico mais complexos => ponto flutuante

a = 3 # nome criado
b = 4 

a + 1
print (a) 
a - 1
print (a)         # adição (3 + 1), subtração (3 - 1)
b * 3, b/2        # multiplicação (4*3), divisão (4/2)
print (b)
a % 2, b ** 2     # módulo (resto), potenciação
print (a)
print (b)
2 + 4.0, 2.0 ** b # conversões de tipo misto

# REPRESENTAÇÃO NUMÉRICA
b / (2.0 + a)          # saída de eco automática (mais dígitos) : 0.80000000000000004
print (b / (2.0 + a))  # saída print arredonda os dígitos : 0.8

num = 1 / 3.0		# 0.3333333333333331
print (num)         # ecoa 0.33333333 print arredondado
"%e" % num          # 3.333333e-001' formatação de string 
"%2.2f" % num       # '0.33' formatação de string

# X / Y	Divisão clássica - mantem o resto, independente dos tipos
# X // Y Divisão na base - operador trunca os restos fracionários em suas bases, independente dos tipos
# Prestar atenção nas versões do Python!!!

(5 / 2)    # 2.5
(5 / 2.0)  # 2.5
(5 / -2.0) # -2.5
(5 / -2)   # -2.5

(5 // 2)    # 2
(5 // 2.0)  # 2.0
(5 // -2.0) # -3.0
(5 // -2)   # -3

(9 / 3)    # 3.0
(9.0 / 3)  # 3.0
(9 // 3)   # 3
(9 // 3.0) # 3.0


# OPERAÇÕES EM NÍVEL DE BIT
x = 1  # 0001
x << 2 # 0100
x | 2  # 0011 - OU em nível de bit (0001)|(0010) = (0011)
x & 1  # 0001 - E em nível de bit 


# INTEIROS LONGOS - inteiros longos podem ser arbitrariamente grandes
# L - cria objeto inteiro com precisão ilimitada
# 999999999999999999999999999999999L + 1  ----->>>> Não funcionou em Python 3
# 10000000000000000000000000000000000L
# Python coverte automaticamente os inteiros normais em inteiros longos
# quando eles estouram a precisão dos inteiros normais
2 ** 200 # 1606938044258990275541962092341162602522202993782792835301376
# o uso de L/l também depende da versão do Python


# NÚMEROS COMPLEXOS
1j * 1J      # (-1 + 0j)
2 + 1j * 3   # (2 + 3j)
(2 + 1j) * 3 # (6 + 3j)


# NOTAÇÃO HEXADECIMAL E OCTAL
# Literias em octal - Funciona em Python 3?
# 01   # 1  --->>> Não funcionou em Python 3
# 010  # 8
# 0100 # 64
# Literias em hexadecimal
0x01 # 1
0x10 # 16
0xFF # 255
#
oct(64)  # '0100'
hex(64)  # '0x40'
hex(255) # '0xff'
#
int('0100')     # 100
int('0100', 8)  # 64
int('0x40', 16) # 64

# eval(expression, globals=None, locals=None)
# In simple terms, the eval() method runs the python code (which is passed as an argument) within the program.
eval('100')  # 100
# eval('0100') # 64 --->>> Não funcionou em Python 3
eval('0x40') # 64 

# conversão de inteiros em strings, em octal e hexadecimal
'100 40 FF'

# OUTRAS FERRAMENTAZ NUMÉRICAS
import math
math.pi # 3.141592653589793
math.e  # 2.718281828459045

math.sin(2*math.pi/180)                   # 0.03489949670250097
abs(-42), 2**4, pow(2, 4)                 # (42, 16, 16)
int(2.567), round(2.567), round(2.567, 2) # (2, 3, 2.5699999999999999998) - 2.57 no print


# REFERÊNCIAS E OBJETOS ALTERÁVEIS
L1 = [2, 3, 4]
L2 = L1 # L2 = [2, 3, 4]
L1[0] = 24
# L1 = [24, 3, 4]
# L2 = [24, 3, 4]
# mais detalhes serão comentados posteriormente


# REFERÊNCIAS E COLETA DE LIXO
# Python recupera o objeto antido, caso ele não seja referenciado por nenhum outro nome
# Essa recuperação automática é conhecida como coleta de lixo
# Isso significa que podemos usar objetos livremente sem jamais liberar espaço em seu script
# Em Python, os tipos pertencem aos objetos e não aos nomes
x = 42
x = 'shrubberry'
x = 3.1415
x = [1, 2, 3]
