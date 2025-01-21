'''
Exercício 5.5) Leia a próxima função e veja se consegue compreender 
o que ela faz (veja os exemplos no Capítulo 4). 
Então execute-a e veja se acertou.
'''

import turtle
import math

wn = turtle.Screen()

bob = turtle.Turtle()
bob.pensize(3)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length*n)
    
draw(bob, 10, 6)

wn.exitonclick()