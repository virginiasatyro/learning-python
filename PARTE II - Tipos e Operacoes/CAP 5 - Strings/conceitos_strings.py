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
myfile = open('C:\new\text.dat', 'w')  # NÃO USAR - tabulações, nova linha, ...
myfile = open(r'C:\new\text.dat', 'w')
myfile = open('C:\\new\\text.dat', 'w') # mesmo que o anterior]


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


