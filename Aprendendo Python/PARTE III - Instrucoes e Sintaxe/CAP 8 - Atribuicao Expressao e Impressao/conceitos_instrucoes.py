'''
Sintaxe Python
1. Os programas são compostos de módulos;
2. Os módulos contêm intruções;
3. As instruções contêm expressões;
4. As expressões criam e processam objetos;
'''

'''
INSTRUÇÃO          FUNÇÃO                       EXEMPLO
Atribuição         Criar referências            curly, moe, larry = 'good', 'bad', 'ugly'
Chamadas           Executar funções             stdout.write("spam")
print              Imprimir objetos             print 'The Killer', joke
if/elif/else       Selecionar ações             if "python" in text: print text
for/else           Iteração de sequência        for x in mylist: print x 
while/else         Loops gerais                 while 1: print 'hello'
pass               Lugar reservado vazio        while 1: pass 
break, continue    Saltos de loop               while 1: if not line: break 
try/except/finally Captura de exceções          try: action() 
                                                except: print 'action error'
raise              Ativar exceção               raise endSearch, location
import/from        Acesso a módulo              import sys; from sys import stdin
def, return, yield Construção de funções        def f(a, b, c = 1, *d): return a + b + c + d[0]
class              Construção de objetos        class subclass: staticData = []
global             Espaços de nome              def function(): global x, y; x = 'new'
del                Exclusão de referências      del data[k]; del data[i:j]
exec               Execução strings de código   exec "import" + modName in gdict, ldict
assert             Verificações de depuração    asser X > Y
'''


# INTRUÇÕES DE ATRIBUIÇÃO
# * As atribuições criam referências de objeto; (variáveis são parecidas com ponteiros)
# * Os nomes são criados ao serem atribuídos pela primeira vez;
# * Os nomes devem ser atribuídos antes de serem referenciados;
# * Atribuições implícitas: import, from, def, class, for, argumentos de função;

''' Formas de instrução de atribuição
OPERAÇÃO                      INTERPRETAÇÃO
spam = 'Spam'                 Forma básica
Spam, ham = 'yum', 'YUM'      Atribuição de tupla (posicional)
[spam, ham] = ['yum', 'YUM']  Atribuição de lista (posicional)
spam = ham = 'lunch'          Destino múltiplo 
'''

nudge = 1
wink = 2
A, B = nudge, wink     # atribuição de tupla
A, B                   # A = nudge; B = wink -> saída = (1, 2)
[C, D] = [nudge, wink] # atribuição de lista
C, D                   # (1, 2)

nudge = 1
wink = 2
nudge, wink = wink, nudge # Tuplas: troca valores
nudge, wink               # Igual a T = nudge; nudge = wink; wink = T
# (2, 1)

[a, b, c] = (1, 2, 3)
a, c # (1, 3)
(a, b, c) = "ABC"
a, c # ('A', 'C')

# red, green, blue = range[3] # equivalente a tipos enumerados?
# red, blue # (0, 2) 

range(3) # [0, 1, 2]

# -> Regras de nome de variável
# * Sintaxe: (sublinhado ou letra) + (qualquer número de letras, algarismos ou sublinhados)
# * Maiúsculo importa;
# * As palavras reservadas estão fora dos limites;

# -> Convenções de atribuição de nomes
# -> Os nomes são têm tipo, mas os objetos têm
# -> Instruções de atribuição ampliadas
'''
x += y     x &= y     x -= y     x|= y
x *= y     x ^= y     x /= y     x >>= y
x %= y     x <<= y    x **= y    x //= y
'''


# INTRUÇÕES DE EXPRESSÃO
# No Python podemos utilizar expressões como instruções;
# * para chamadas de funções e métodos;
# * para imprimir valores no prompt interativo;
'''
OPERAÇÃO                    INTERPRETAÇÃO
spam(eggs, ham)             Chamadas de função
spam.ham(eggs)              Chamadas de métodos
Spam                        Impressão interativa
spam < ham and ham != eggs  Expressões compostas
spam < ham < eggs           Testes de intervalo 
'''


# INSTRUÇÃO DE IMPRESSÃO
'''
OPERAÇÃO                    INTERPRETAÇÃO
print spam, ham             Imprime objetos em sys.stdout; adiciona um espaço entre eles
print spam, ham,            Igual, mas não adiciona caractere de nova linha no final do texto
print >> myfile, spam, ham  Envia texto para myfile, write e não para sys.stdout.write
'''
x = 1; y = 2
print (x + y)             # ab
# print (('%s...s') % (x, y)) # a...b

# -> Redirecionando o fluxo de saída
print (x) 
# expressão equivalente à:
import sys
sys.stdout.write(std(x) + '\n') # não funciona em Python 3?

import sys
sys.stdout = open('log.txt', 'a') # redirecionan impressão para arquivo
print (x, y, x)                   # aparece em log.txt
sys.stdout = temp
print (a, b, c)                   # imprime no stdout original