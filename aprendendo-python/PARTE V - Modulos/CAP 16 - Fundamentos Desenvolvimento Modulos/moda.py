x = 88        # meu x: global apenas para esse arquivo

def f():
	global x  # altera meu x
	x = 99    # não pode ver nomes em outros módulos