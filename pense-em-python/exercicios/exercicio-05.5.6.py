'''
Exercício 5.6) A curva de Koch é um fractal que parece com o da Figura 5.2 (Uma curva de Koch). 
Para desenhar uma curva de Koch com o comprimento x, tudo o que você tem que fazer é:

Desenhe uma curva de Koch com o comprimento x/3.
Vire 60 graus à esquerda.
Desenhe uma curva de Koch com o comprimento x/3.
Vire 120 graus à direita.
Desenhe uma curva de Koch com o comprimento x/3.
Vire 60 graus à esquerda.
Desenhe uma curva de Koch com o comprimento x/3.

A exceção é se x for menor que 3: neste caso, você pode desenhar apenas uma linha 
reta com o comprimento x.

Escreva uma função chamada koch que receba um turtle e um comprimento como parâmetros, 
e use o turtle para desenhar uma curva de Koch com o comprimento dado.

Escreva uma função chamada snowflake que desenhe três curvas de Koch para fazer o 
traçado de um floco de neve.

Solução: http://thinkpython2.com/code/koch.py.

A curva de Koch pode ser generalizada de vários modos.
Veja exemplos em http://en.wikipedia.org/wiki/Koch\_snowflake e implemente o seu favorito.
'''

import turtle
import math

screen = turtle.Screen()
screen.title("Snowflake using Turtle")
screen.bgcolor("blue")

bob = turtle.Turtle()
bob.pensize(3)
bob.color("white")

def kochFractal(t, x):
    if x > 3:
        t.forward(x / 3)
        t.left(60)
        t.forward(x / 3)
        t.right(120)
        t.forward(x / 3)
        t.left(60)
        t.forward(x / 3)
    else:
        t.forward(x)
        return
    
def fractal(t, length, depth):
    if depth == 0:
        t.forward(length)
        return 
    length /= 3.0
    
    fractal(t, length, depth - 1)
    t.left(60)
    fractal(t, length, depth - 1)
    t.right(120)
    fractal(t, length, depth - 1)
    t.left(60)
    fractal(t, length, depth - 1)
        
def snowFlake(t, length):
    for i in range(6):
        # kochFractal(t, length)
        fractal(t, length, 3)
        t.rt(60)
    
# kochFractal(bob, 100)
snowFlake(bob, 150)
    
screen.exitonclick()