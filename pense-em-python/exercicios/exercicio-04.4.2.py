'''
Exercício 4.2: Escreva um conjunto de funções adequadamente geral que 
possa desenhar flores como as da Figura 4.1 (Flores de tartaruga).
'''

import turtle
import math

wn = turtle.Screen()

bob = turtle.Turtle()
bob.pensize(3)
bob.color("Red")
    
def arc(t, r,  angle):
    for i in range(angle):
        t.fd(2*math.pi*r/360)
        t.lt(1)
        
def flower(t, numPetals, lenPetals, angle):
    for i in range(numPetals):
        for i in range(2):
            arc(t, lenPetals, angle)
            t.lt(180 - angle)
        t.lt(360/numPetals)
        
flower(bob, 6, 200, 45)

wn.exitonclick()