'''
4. Escreva uma função chamada circle que use o turtle, t e um raio r 
como parâmetros e desenhe um círculo aproximado ao chamar polygon com 
um comprimento e número de lados adequados. Teste a sua função com uma 
série de valores de r.
Dica: descubra a circunferência do círculo e certifique-se de que 
length * n = circumference.
'''

import turtle
import math

wn = turtle.Screen()

bob = turtle.Turtle()
bob.pensize(3)

def polygon(t, len, n):
    for i in range(n):
        t.fd(len)
        t.lt(360/n)
        
def circle(t, r):
    polygon(t, 2*math.pi*r/360, 360)
        
circle(bob, 50)

wn.exitonclick()

'''
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 5-
    length = circumference / n
    polygon(t, n, length)
'''