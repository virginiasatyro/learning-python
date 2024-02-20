'''
Exercício 4.3: Escreva um conjunto de funções adequadamente geral 
que possa desenhar formas como as da Figura 4.2 (Tortas de tartaruga).
'''

import turtle
import math

wn = turtle.Screen()

bob = turtle.Turtle()
bob.pensize(3)

def isoceles(t, leg, baseAngle, base):
    t.fd(leg)
    t.lt(180 + baseAngle)
    t.fd(base)
    t.lt(180 + baseAngle)
    t.fd(leg)
    
def polypie(t, n, leg):
    vertexAngle = 360 / n
    baseAngle = (180 - vertexAngle) / 2
    base = math.sqrt(2 * (leg ** 2) - ((2 * (leg**2)) * math.cos(vertexAngle * (math.pi / 180))))
    for i in range(n):
        isoceles(t, leg, baseAngle, base)
        t.rt(180 - 2 * vertexAngle)
        
polypie(bob, 5, 100)

wn.exitonclick()