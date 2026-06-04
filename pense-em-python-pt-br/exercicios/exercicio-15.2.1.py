import turtle
import math

screen = turtle.Screen()

t = turtle.Turtle()
t.pensize(3)

class Point:
  """ represents a point in 2D space """
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    
class Rectangle:
  """ represents a rectangle. 
    attributes: width, height, corner.
  """
  def __init__(self, corner, width, height):
    self.corner = corner
    self.width = width
    self.height = height

def draw_rect(t, rect):
  """ Draws a Rectangle using turtle t. """
  for i in range(2):
    t.forward(rect.width)
    t.left(90)
    t.forward(rect.height)
    t.left(90)

box = Rectangle(Point(0, 0), 100, 200)
draw_rect(t, box)

screen.exitonclick()