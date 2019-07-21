spam = "That is Alice's cat."
spam = 'Say hi to Bob\'s mother.'

'''
\'    aspas simples
\"    aspas duplas 
\t    tabulação 
\n    quebra ou mudança de linha 
\\    barra invertida
'''

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
''' Output:
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
'''

spam = 'Hello world!'
spam[0]   # 'H'
spam[4]   # 'o'
spam[-1]  # '!'
spam[0:5] # 'Hello'
spam[:5]  # 'Hello'
spam[6:]  #'world!'

spam = 'Hello world!'
fizz = spam[0:5]
fizz # 'Hello' 

'Hello' in 'Hello World' # True
'Hello' in 'Hello' # True
'HELLO' in 'Hello World' # False
'' in 'spam' # True
'cats' not in 'cats and dogs' # False

spam = spam.upper()
spam # 'HELLO WORLD!'
spam = spam.lower()
spam # 'hello world!'

print('How are you?')
feeling = input()
if feeling.lower() == 'great': # 'GREat' 'GREAT' 'greAT'
	print('I feel great too.')
else:
	print('I hope the rest of your day is good.')

spam = 'Hello world!'
spam.islower()       # False
spam.isupper()       # False
'HELLO'.isupper()    # True
'abc12345'.islower() # True
'12345'.islower()    # False
'12345'.isupper()    # False

'Hello'.upper()                 # 'HELLO'
'Hello'.upper().lower()         # 'hello'
'Hello'.upper().lower().upper() # 'HELLO'
'HELLO'.lower()                 # 'hello'
'HELLO'.lower().islower()       # True

'''
* isalpha() retornará True se a string for constituída somente de letras e não
estiver vazia.
* isalnum() retornará True se a string for constituída somente de letras e
números e não estiver vazia.
* isdecimal() retornará True se a string for constituída somente de caracteres
numéricos e não estiver vazia.
* isspace() retornará True se a string for constituída somente de espaços,
tabulações e quebras de linha e não estiver vazia.
* istitle() retornará True se a string for constituída somente de palavras que
comecem com uma letra maiúscula seguida somente de letras minúsculas.
'''

'hello'.isalpha()    # True
'hello123'.isalpha() # False
'hello123'.isalnum() # True
'hello'.isalnum()    # True
'123'.isdecimal()    # True
' '.isspace()        # True

'This Is Title Case'.istitle()            # True
'This Is Title Case 123'.istitle()        # True
'This Is not Title Case'.istitle()        # False
'This Is NOT Title Case Either'.istitle() # False

while True:
	print('Enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number for your age.')

while True:
	print('Select a new password (letters and numbers only):')
	password = input()
	if password.isalnum():
		break
	print('Passwords can only have letters and numbers.')
	
'Hello world!'.startswith('Hello')        # True
'Hello world!'.endswith('world!')         # True
'abc123'.startswith('abcdef')             # False
'abc123'.endswith('12')                   # False
'Hello world!'.startswith('Hello world!') # True
'Hello world!'.endswith('Hello world!')   # True










