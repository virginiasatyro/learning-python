'''
1. Escreva uma função chamada square que receba um parâmetro chamado t, 
que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
Escreva uma chamada de função que passe bob como um argumento para o 
square e então execute o programa novamente.
'''

import turtle

wn = turtle.Screen()

bob = turtle.Turtle()
bob.pensize(3)

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
square(bob)

wn.exitonclick()