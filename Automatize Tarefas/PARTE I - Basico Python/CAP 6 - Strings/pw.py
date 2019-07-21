'''
Queremos executar esse programa com um argumento de linha de comando
correspondente ao nome da conta – por exemplo, email ou blog. A senha
dessa conta será copiada para o clipboard para que o usuário possa colá-la em
um campo de Senha. Dessa maneira, o usuário poderá ter senhas longas e
complexas sem a necessidade de memorizá-las.
'''

#! python3
# pw.py – Um programa para repositório de senhas que não é seguro.
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
			 
import sys, pyperclip

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()
	
account = sys.argv[1] # o primeiro argumento da linha de comando é o nome da conta

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
else:
	print('There is no account named ' + account)