# ATENÇãO >> problemas de compilação devido ao unicode - provavelmente por causa de diferença de versão do python

'''
OPERAÇÃO                   INTERPRETAÇÃO
s1 = ' '                   String vazia
s2 = "spam's"              Aspas duplas
block = """..."""          Blocos com aspas triplas
s3 = r'\temp\spam'         Strings brutas
s4 = u'spam'               Strings Unicode
s1 + s2                    Concatenação
s2 * 3                     Repetição
s2[i]                      Índice
s2[i:j]                    Fracionamento
len(s2)                    Comprimento
"a %s parrot" % 'dead'     Formatação de string
s2.find('pa')              Chamadas de métodos de string
s2.replace('pa', 'xx')
s1.split()
for x in s2                Iteração
'm' in s2                  Participação como membro
'''

# Sequências de escape: "s\tp\na\om"
# Strings brutas: r"C:\new\test.spm"
# Strings Unicode: u'eggs\u0020spam'

# Strings com apóstrofos e aspas são iguais
'shrubbery'
"shrubbery"
'knight"s'
"knight's"

title = "Meaning " 'of' " Life"
title # Meaning of Life

'knight\'s' # "knight's"
"knight\"s" # 'knight"s'


'''
ESCAPE
\newline   Ignorado(continuação)
\\         Barra invertida(mantém uma \)
\'         Apóstrofo (mantém ')
\"         Aspas(mantém ")
\a         Bip
\b         Retrocesso
\f         Avanço de formulário
\n         Nova linha (avanço de linha)
\r         Carriage return 
\t         Tabulação horizontal
\v         Tabulação vertical
\n{id}     Id dbase Unicode
\uhhhh     Hexadecimal de 16 bits Unicode
\Uhhhh...  Hexadecimal de 32 bits Unicode
\xhh       Valor de dígitos em hexadecimal hh
\ooo       Valor de dígitos em octal
\0         Nulo (não termina string)
\other     Não é escape (mantido)
'''

# No python, o byte zero não termina uma string como normalmente acontece em C.
# Python mantém o comprimento e o texto da string na memória.
# Nenhum caracter termina uma string em Python.

s = '\001\002\x03' # '\x01\x02\x03'
x = "C:\py\code"   # 'C:\py\code' len(x) = 10  -> mantém \ literalmente

# STRINGS BRUTAS
# r - aparece imediatamente antes das aspas ou apóstrofo de abertura de uma string,
# ela desativa o mecanismo de escape.
myfile = open('C:\new\text.dat', 'w')   # NÃO USAR - tabulações, nova linha, ...
myfile = open(r'C:\new\text.dat', 'w')
myfile = open('C:\\new\\text.dat', 'w') # mesmo que o anterior


# ASPAS TRIPLAS
# Definem strings de bloco de várias linhas
mantra = """Always look
...on the bright
..side of life."""
# mantra : 'Always look\non the bright\nside of life.'


# STRINGS UNICODE
# Definem conjuntos de caracteres maiores
# Strings em unicode são usadas para suportar a internacionalização de aplicativos.
u'spam' # 'spam'

str(u'spam')    # de unicode para normal
unicode('spam') # de normal para unicode 
# Unicode é projetado para manipular caracteres de vários bytes
u'ab\x20cd'       # caracteres de 8 bits\1 bytes = u'ab cd'
u'ab\u0020cd'     # caracteres de 2 bytes = u'ab cd'
u'ab\U00000020cd' # caracteres de 4 bytes = u'ab cd


# STRINGS EM AÇÃO
len('abc')    # Comprimento = 3
'abc' + 'def' # Concatenação = 'abcdef'
'Ni!' * 4     # Repetição: 'Ni!Ni!Ni!Ni!'

print ('-------...sequencia...-------') # 80 traços do jeito difícil
print ('-' * 80) # 80 traços do jeito fácil

myjob = "hacker"
for c in myjob: print (c) # percorre os itens = h a c k e raise
"k" in myjob # 1 significa true = 1 
"z" in myjob # 0 significa false = 0

# Indexação e fracionamento
# Strings - coleção ordenada de caracteres; podemos buscar caracteres por indexação;
S = 'spam'           
S[0], S[-2]           # indexação a partir do início ou do fim = ('s', 'a')
S[1:3], S[1:], S[:-1] # Facionamento = ('pa', 'pam', 'spa')
# S[-2] = S[len(S) - 2]
# S[i:j] - limite superior não-inclusivo 

# Ferramenta de conversão de string
"42" + 1 # ERRO
int("42"), str(42)        # Converte de/para string = (42, '42')
string.atoi("42"), '42'   # O mesmo,, mas são técnicas mais antigas = (42, '42')
int("42") + 1             # Força de adição = 43
"spam" + str(42) 		  # Força a concatenação = 'spam42'
str(3.1415), float("1.5") # ('3.1415', 1.5)
text = "1.234E-10"
float(text)               # 1.23400000000001e-010

# Alterando strings
S = 'spam'
S[0] = "x"      # ERRO
S = s + 'SPAM!' # para alterar uma string, faça uma nova
S # 'spamSPAM'
S = S[:4] + 'Burger' + S[-1]
S # 'spamBurger'!

'That is %d %s bird!' % (1, 'dead') # como a instrução sprintf da linguagem C
# That is 1 dead bird!


# FORMATAÇÃO DE STRING 
exclamation = "Ni"
"The knights who say %s!" % exclamation 
# 'The knights who say Ni!'
"%d %s %d you" % (1, 'spam', 4)
# '1 spam 4 you'
"%s -- %s -- %s" % (42, 3.14159, [1, 2, 3])
# '42 -- 3.14159 -- [1, 2, 3]'

# Formatação de string avançada
'''
CÓDIGO SIGNIFICADO
%s     String (ou qualquer objeto)
%r     s, mas usa repr() e não str()
%c     Caractere
%d     Decimal (inteiro)
%i     Inteiro
%u     Sem sinal (inteiro)
%o     Inteiro em octal
%x     Inteiro em hexadecimal
%X     x, mas imprime em maiúsculo
%e     Expoente de ponto flutuante 
%E     e, mas imprime em maiúsculo
%f     Decimal de ponto flutuante
%g     e ou f de ponto flutuante
%G     E ou f de ponto flutuante
%%     '%' literal
'''

# Estrutura geral dos destinos de conversão:
# [(nome)][flag][largura][[.precisao]]código
x = 1234
res = "integers:...%d...%-6d...%06d" % (x, x, x)
res # 'integers:...1234...1234...001234'

x = 1.23456789
x # 1.23456789999999999
'%e | %f | %g' % (x, x, x) 
# '1.234568e+000 | 1.234568 | 1.23457'
'%-6.2f | %05.2f | %+06.1f'  % (x, x, x)
# '1.23 | 01.23 | +001.2'
"%s" % x, str(x)
# ('1.23456789', '1.23456789')
"%(n)d %(x)s" % {"n": 1, "x": "spam"}
# '1 spam'
food = 'spam'
age = 40
vars()
# {'food': 'spam', 'age': 40, ... muito mais...}
"(age)d%(food)s" % vars()
# '40 spam'


# MÉTODOS DE STRINGS
# Métodos implementam tarefas de processamento mais sofisticadas;
# BUSCAS DE ATRIBUTO: espressão na forma objeto.atributo significa "buscar o valor de atributo em objeto" 
# EXPRESSÕES DE CHAMADA: espressão na forma função(argumento) significa "ative" o código de função,
# passando a ela zero ou mais objetos argumento separados por vírgulas e retornando o valor do resultado
# da função;

'''
CHAMADAS DE MÉTODO DE STRING
S.capitalize()
S.center(width)
S.count(sub[, start [end]])
S.encode([encoding [, errors]])
.
.
.
'''

S = 'spammy'
S = S[:3] + 'xx' + S[5:]
S # 'spaxxy'

S = 'spammy'
S = S.replace('mm', 'xx') # substitui substring
S # 'spaxxy'

'aa$bb$cc$dd'.replace('$', 'SPAM')
# 'aaSPAMbbSPAMccSPAMdd'

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM') # procura posição
where # 4
S = S[:where] + 'EGGS' + S[(where + 4):]
S # 'xxxxEGGSxxxxSPAMxxxx'

S = 'xxxxSPAMxxxxSPAMxxxx'
S.replace('SPAM', 'EGGS') # substitui tudo
S # 'xxxxEGGSxxxxEGGSxxxx'
S.replace('SPAM', 'EGGS', 1) # substitui uma
S # 'xxxxEGGSxxxxSPAMxxxx'

# melhora do desempenho do script convertendo a string em um objeto que suporte alteração no local
S = 'spammy'
L = list(S)
L # ['s', 'p', 'a', 'm', 'm', 'y']
L[3] = 'x' # funciona para listas e não para strings
L[4] = 'x'
L # ['s', 'p', 'a', 'x', 'x', 'y']
# conversão de volta para string
S = ' '.join(L)
S # 'spaxxy'
'SPAM'.join(['eggs', 'sausage', 'ham', 'toast'])
S # eggsSPAMsausageSPAMhamSPAMtoast

# Análise de texto
line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
col1 # 'aaa'
col3 # 'ccc'

line = 'aaa bbb ccc'
cols = line.split()
cols # ['aaa', 'bbb', 'ccc']

line = 'bob, hacker, 40'
line.split(',')
['bob', 'hacker', '40']

line = "i'mSPAMaSPAMlumberjack"
line.split("SPAM") # ["i'm", 'a', 'lumberjack']