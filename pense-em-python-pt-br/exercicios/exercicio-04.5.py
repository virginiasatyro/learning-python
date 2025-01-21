'''
Faça uma versão mais geral do circle chamada arc, 
que receba um parâmetro adicional de angle, para
determinar qual fração do círculo deve ser desenhada. 
angle está em unidades de graus, então quando angle=360, 
o arc deve desenhar um círculo completo.
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
    
def arc(t, r,  angle):
    for i in range(angle):
        t.fd(2*math.pi*r/360)
        t.lt(1)
        
arc(bob, 150, 270)

wn.exitonclick()