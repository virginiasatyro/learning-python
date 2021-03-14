# Python Basics for Data Science

## Module 1 - Python Basics

https://labs.cognitiveclass.ai/ 

Learning objectives:

- Types
- Expressions and Variables
- String Operations

### Types 
```
# Try your first Python output

print('Hello, Python!')
```
```
# Check the Python Version

import sys
print(sys.version)
```
```
# Practice on writing comments

print('Hello, Python!') # This line prints a string
# print('Hi')
```
```
# Integer

11
```
```
# Float

2.14
```
```
# String

"Hello, Python 101!"
```
```
# Type of 12

type(12)
```
```
# Type of 2.14

type(2.14)
```
```
# Type of "Hello, Python 101!"

type("Hello, Python 101!")
```
```
# Print the type of -1

type(-1)
```
```
# Print the type of 4

type(4)
```
```
# Print the type of 0

type(0)
```
```
# Print the type of 1.0

type(1.0) # Notice that 1 is an int, and 1.0 is a float
```
```
# Print the type of 0.56

type(0.56)
```
```
# Print the type of 0.5

type(0.5)
```
```
# System settings about float type

sys.float_info
```
```
# Convert 2 to a float

float(2)
```
```
# Convert integer 2 to a float and check its type

type(float(2))
```
```
# Convert a string into an integer

int('1')
```
```
# Convert the string "1.2" into a float

float('1.2')
```
```
# Convert an integer to a string

str(1)
```
```
# Type of True

type(True)
```
```
# Convert True to int

int(True)
```

### Expressions and Variables

```
# Addition operation expression

43 + 60 + 16 + 41
```
```
# Subtraction operation expression

50 - 60
```
```
# Multiplication operation expression

5 * 5
```
```
# Integer division operation expression

25 // 5
```
```
# Store value into variable

x = 43 + 60 + 16 + 41
```
```
# Print out the value in variable

x
```
```
# Use another variable to store the result of the operation between variable and value

y = x / 60
y
```
```
# Name the variables meaningfully

total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min
```
```
# Complicate expression

total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours
```

### String Operations

```print("Hello")```

```print("Hello\nWorld")```

```# this is a comment```

```
# Use quotation marks for defining string

"Michael Jackson"
```

```
# Use single quotation marks for defining string

'Michael Jackson'
```
```
# Digitals and spaces in string

'1 2 3 4 5 6 '
```
```
# Special characters in string

'@#2_#]&*^%$'
```
```
# Print the string

print("hello!")
```
```
# Assign string to variable

Name = "Michael Jackson"
Name
```
```
# Print the first element in the string

print(Name[0])
```
```
# Print the element on the 13th index in the string

print(Name[13])
```
```
# Print the last element in the string

print(Name[-1])
```
```
# Print the first element in the string

print(Name[-15])
```
```
# Find the length of string

len("Michael Jackson")
```
```
# Take the slice on variable Name with only index 0 to index 3

Name[0:4]
```
```
# Take the slice on variable Name with only index 8 to index 11

Name[8:12]
```
```
# Get every second element. The elments on index 1, 3, 5 ...

Name[::2]
```
```
# Get every second element in the range from index 0 to index 4

Name[0:5:2]
```
```
# Concatenate two strings

Statement = Name + "is the best"
Statement
```
```
# Print the string for 3 times

3 * "Michael Jackson"
```
```
# Concatenate strings

Name = "Michael Jackson"
Name = Name + " is the best"
Name
```
```
# New line escape sequence

print(" Michael Jackson \n is the best" )
```
```
# Tab escape sequence

print(" Michael Jackson \t is the best" )
```
```
# Include back slash in string

print(" Michael Jackson \\ is the best" )
```
```
# r will tell python that string will be display as raw string

print(r" Michael Jackson \ is the best" )
```
```
# Convert all the characters in string to upper case

A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)
```
```
# Replace the old substring with the new target substring is the segment has been found in the string

A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B
```
```
# Find the substring in the string. Only the index of the first elment of substring in string will be the output

Name = "Michael Jackson"
Name.find('el')
```
```
# Find the substring in the string.

Name.find('Jack')
```
```
# If cannot find the substring in the string

Name.find('Jasdfasdasdf')
```
