'''
3. uma cópia do square e mude o nome para polygon. 
Acrescente outro parâmetro chamado n e altere o corpo 
para que desenhe um polígono regular de n lados.
Dica: os ângulos exteriores de um polígono regular de n 
lados são 360/n graus.
'''

import turtle

wn = turtle.Screen()

bob = turtle.Turtle()
bob.pensize(3)

def polygon(t, len, n):
    for i in range(n):
        t.fd(len)
        t.lt(360/n)
        
polygon(bob, 100, 7)

wn.exitonclick()