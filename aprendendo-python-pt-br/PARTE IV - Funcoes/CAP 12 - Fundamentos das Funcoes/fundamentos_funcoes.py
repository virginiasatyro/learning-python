# Instruções e expressões relacionadas ás funções
'''
INTRUÇÃO            EXEMPLOS
Chamadas            myfunc("spam", ham, "toast")
def, return, yield  def adder(a, b = 1 *c): return a + b + c[0]
global              def function(): global x; x = 'new'
lambda              funcs = [lambda x: x**2, lambda x: x*3]
'''

''' 
Funções:
- Por que utilizar?
    * Reutilização de código;
	* Decomposição procedural;
- Desenvolvendo funções:
    * DEF é código executável - sua função não existe até que o Python busque e execute a instrução def;
	* DEF cria um objeto e atribui um nome a ele;
	* RETURN envia um objeto resultado de volta para quem fez a chamada;
	* Os argumentos são passados por atribuição (referência de objeto);
	* GLOBAL declara variáveis em nível de módulo que devem ser atribuídas;
	* Argumentos, valores de retorno e variáveis não são declarados;
'''

# INSTRUÇÕES DEF 
''' Forma geral:
def <nome>(arg1, arg2, ..., argN):
    <instruções>
	return <valor> (opcional)
'''
# instrução DEF é executada em tempo de execução

# PRIMEIRO EXEMPLO: DEFINIÇÕES E CHAMADAS
# * Definição:
def times(x, y): # cria e atribui função
    return x*y   # corpo executado quando chamado
	
# * Chamadas:
print(times(2, 4))
print(times(2, 2))
print(times(32, 64))
x = times(3.1415, 4)
print(x)
print(times('Na', 4)) # polimorfismo
# Polimorfismo no Python - o significado das operações depende dos objetos que estão sendo utilizados;
# Toda operação é polimórfica em Python!

# SEGUNDO EXEMPLO: INTERSEÇÃO DE SEQUÊNCIAS
# Definição:
def intersec(seq1, seq2): # ATENÇÃO - utilizar SPACE desde o início da linha (contando todos os espaços)
    res = [] # começa vazio
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res 

# * Chamadas:
s1 = "SPAM"
s2 = "SCAM"
print(intersec(s1, s2)) # strings = ['S', 'A', 'M']
# Polimorfismo - intersec é polimórfica - funciona em tipos arbitrários
x = intersec([1, 2, 3], (1, 4))
print (x) # [1]

# VARIÁVEIS LOCAIS
# res dentro da função intersec é chamada de variável local -
# só existe enquanto a função é executada;


	


