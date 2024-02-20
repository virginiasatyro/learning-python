'''
2. Acrescente outro parâmetro, chamado length, ao square. 
Altere o corpo para que o comprimento dos lados seja length 
e então altere a chamada da função para fornecer um segundo 
argumento. Execute o programa novamente. Teste o seu programa 
com uma variedade de valores para length.
'''

import turtle

wn = turtle.Screen()

bob = turtle.Turtle()
bob.pensize(3)

def square(t, len):
    for i in range(4):
        t.fd(len)
        t.lt(90)
        
square(bob, 200)

wn.exitonclick()