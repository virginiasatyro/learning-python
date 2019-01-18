# MÓDULOS
# Unidade de organização de programa de nível mais alto, a qual empacota  
# código de programa e dados para reutilização;
# Normalmente correspondem aos arquivos de programa do Python;

# IMPORT - permite que um cliente (importador) busque um módulo como um todo;
# FROM - permite que os clientes busquem nomes específicos de um módulo;
# RELOAD - fornece uma maneira de recarregar o código de um módulo sem
# interromper o Python;

''' Por que usar módulos?
* Reutilização de código;
* Particionamento do espaço de nome do sistema;
* Implementar serviços ou dados compartilhados;
'''


# ARQUITERURA DE PROGRAMA EM PYTHON
# Como estruturar um programa:
'''
- Programa - vários arquivos contendo instruções em Python;
- Programa é estruturado como um arquivo de NÍVEL SUPERIOR principal, 
junto com zero ou mais arquivos complementares -> MÓDULOS;
- Arquivo de nível superior -> contém fluxo de controle principal do 
programa (arquivo executado);
- Arquivos de módulo -> bibliotecas de ferramentas usadas para reunir 
componentes utilizados pelo arquivo de nível superior;
- Arquivos de nível superior - utilizam ferramentas definidas em módulos;
- Módulos - utilizam ferramentas definidas em outros módulos;
- Um arquivo IMPORTA um módulo para ter acesso às ferramentas; 
'''
# Importações e atributos:
'''
Nível superios    Módulos 
a.py              b.py      -> Módulos da biblioteca padrão
                  c.py    

a.py
def spam(text):
    print text, 'spam'	

b.py 
import b 
b.spam('gumby')	
'''
# Módulos da biblioteca padrão
# Alguns dos módulos importados são fornecidos pelo próprio Python, e não por 
# arquivos que você escreverá;


# COMO AS IMPORTAÇÕES FUNCIONAM
'''
Não funcionam como o #include do C, são operações em tempo de execução
que realizam três etapas distintas na primeira vez que um arquivo é 
importado por um programa:
1. Localizar o arquivo do módulo;
2. Compilá-lo no código de byte (se mecessário);
3. Executar o código do módulo para construir os objetos que ele define;
'''