# Python Basics for Data Science

## Module 3 - Python Programming Fundamentals 

- Conditions and Branching
- Loops
- Functions
- Objects and Classes

### Conditions and Branching

- equal: ==
- not equal: !=
- greater than: >
- less than: <
- greater than or equal to: >=
- less than or equal to: <=
```
# Condition Equal

a = 5
a == 6
```
```
# Greater than Sign

i = 6
i > 5
```
```
# Greater than Sign

i = 2
i > 5
```
```
# Inequality Sign

i = 2
i != 6
```
```
# Inequality Sign

i = 6
i != 6
```
```
# Use Equality sign to compare the strings

"ACDC" == "Michael Jackson"
```
```
# Use Inequality sign to compare the strings

"ACDC" != "Michael Jackson"
```
```
# Compare characters

'B' > 'A'
```
```
# Compare characters

'BA' > 'AB'
```
```
# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")
```
```
# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")
```
```
# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")
```
```
# Condition statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')
```
```
# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')
```
```
# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")
```
```
# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
```
```
# Condition statement example

album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")
```

### Loops
```
# Use the range

range(3) # range(0, 3)
```
```
# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i]) # 1982,1980,1973
```
```
# Example of for loop

for i in range(0, 8):
    print(i) # 0 1 2 3 4 5 6 7 
```
```
# Exmaple of for loop, loop through list

for year in dates:  
    print(year) # 1982,1980,1973
```
```
# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])
```
```
# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square) # 0 red 1 yellow 2 green 3 purple 4 blue
```
```
# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year) # 1982 1980 1973

print("It took ", i ,"repetitions to get out of loop.") # 3
```
```
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)
```
```
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1
```

### Functions
```
# First function example: Add 1 to a and store as b

def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)
```
```
# Get a help on add function

help(add) # Help on function add in module __main__: add(a)
```
```
# Call the function add()

add(1) # 1 if you add one 2    2
```
```
# Call the function add()
 
add(2) # 2 if you add one 3    3
```
```
# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
```
```
# Use mult() multiply two integers

Mult(2, 3) # 6
```
```
# Use mult() multiply two floats

Mult(10.0, 3.14) # 31.400000000000002
```
```
# Use mult() multiply two different type values together

Mult(2, "Michael Jackson ") # 'Michael Jackson Michael Jackson '
```
```
# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)
```
```
# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x) # 3 if you square + 1 10
y # 10
```
```
# Directly enter a number as parameter

square(2) # 2 if you square + 1 5
```
```
# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

MJ()  # Michael Jackson
MJ1() # Michael Jackson

print(MJ())  # None 
print(MJ1()) # None
```
```
# Define the function for combining strings

def con(a, b):
    return(a + b)
```
```
# Test on the con() function

con("This ", "is") # 'This is'
```

### Objects and Classes
```
# Import the library

import matplotlib.pyplot as plt
%matplotlib inline  
```
```
# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
```
```
# Create an object RedCircle

RedCircle = Circle(10, 'red')
```
```
# Find out the methods can be used on the object RedCircle

dir(RedCircle)

'''['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'add_radius',
 'color',
 'drawCircle',
 'radius']'''
```
```
# Print the object attribute radius

RedCircle.radius # 10
```
```
# Print the object attribute color

RedCircle.color # 'red'
```
```
# Set the object attribute radius

RedCircle.radius = 1
RedCircle.radius # 1
```
```
# Call the method drawCircle

RedCircle.drawCircle()
```
```
# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius) # Radius of object: 2
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius) # Radius of object of after applying the method add_radius(2): 4
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius) # Radius of object of after applying the method add_radius(5): 9
```
```
# Create a blue circle with a given radius

BlueCircle = Circle(radius=100)
```
```
# Print the object attribute radius

BlueCircle.radius # 100
```
```
# Print the object attribute color

BlueCircle.color # 'blue'
```
```
# Call the method drawCircle

BlueCircle.drawCircle()

```
```
# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
```
```
# Create a new object rectangle

SkinnyBlueRectangle = Rectangle(2, 10, 'blue')
```
```
# Print the object attribute height

SkinnyBlueRectangle.height # 10
```
```
# Print the object attribute width

SkinnyBlueRectangle.width # 2
```
```
# Print the object attribute color

SkinnyBlueRectangle.color # 'blue'
```
```
# Use the drawRectangle method to draw the shape

SkinnyBlueRectangle.drawRectangle()
```
```
# Create a new object rectangle

FatYellowRectangle = Rectangle(20, 5, 'yellow')
```
```
# Print the object attribute height

FatYellowRectangle.height 
```
```
# Print the object attribute width

FatYellowRectangle.width # 20
```
```
# Print the object attribute color

FatYellowRectangle.color # 'yellow'
```
```
# Use the drawRectangle method to draw the shape

FatYellowRectangle.drawRectangle()
```