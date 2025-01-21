'''
Exercício 4.5: Leia sobre espirais em https://pt.wikipedia.org/wiki/Espiral; 
então escreva um programa que desenhe uma espiral de Arquimedes (ou um dos outros tipos).
'''

import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.title("Spiral of Archimedes using Turtle")
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Set up the turtle
bob = turtle.Turtle()
bob.speed(0)  # Set the turtle speed to the maximum

# Constants for the spiral
a = 0.1
b = 0.5

# Draw the spiral
theta = 0
for _ in range(1000):
    r = a + b * theta
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    bob.goto(x * 10, y * 10)  # Scale up the coordinates for better visibility
    theta += 0.1

# Hide the turtle and display the result
bob.hideturtle()
screen.mainloop()

screen.exitonclick()

'''import turtle
import math

wn = turtle.Screen()

bob = turtle.Turtle()
bob.pensize(3)

def isoceles(t, leg, baseAngle, base):
    bob.fd(leg)
    bob.lt(180 + baseAngle)
    bob.fd(base)
    bob.lt(180 + baseAngle)
    bob.fd(leg)
    
def polypie(t, n, leg):
    vertexAngle = 360 / n
    baseAngle = (180 - vertexAngle) / 2
    base = math.sqrt(2 * (leg ** 2) - ((2 * (leg**2)) * math.cos(vertexAngle * (math.pi / 180))))
    for i in range(n):
        isoceles(t, leg, baseAngle, base)
        bob.rt(180 - 2 * vertexAngle)
        
def polygon(t, len, n):
    for i in range(n):
        bob.fd(len)
        bob.lt(360/n)
        
def circle(t, r):
    polygon(t, 2*math.pi*r/360, 360)
    
def espiral(t, n, length = 3, a = 0.1, b = 0.0002):
    for i in range(r):
        polygon(t, 2*math.pi*i/360, i)
        i = i + 1
      
        
# polypie(bob, 5, 100)
espiral(turtle, 100)

wn.exitonclick()'''

'''
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Spiral using Turtle")
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Set up the turtle
t = turtle.Turtle()
bob.speed(0)  # Set the turtle speed to the maximum

# Draw a spiral
length = 10
angle = 90
for _ in range(100):
    bob.forward(length)
    bob.right(angle)
    length += 5

# Hide the turtle and display the result
bob.hideturtle()
screen.mainloop()'''
