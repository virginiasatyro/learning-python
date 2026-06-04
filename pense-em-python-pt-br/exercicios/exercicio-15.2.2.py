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
    
def draw_circle(t, circle):
  """ Draws a Circle using turtle t. """
  t.up()
  t.forward(circle.radius)
  t.left(90)
  t.down()
  t.circle(circle.radius)

class Circle:
  """ represents a circle.
    attributes: center, radius.
  """
  def __init__(self, center, radius):
    self.center = center
    self.radius = radius

circle = Circle(Point(0, 0), 50)
draw_circle(t, circle)

screen.exitonclick()