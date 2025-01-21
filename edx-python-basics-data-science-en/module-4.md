# Python Basics for Data Science

## Module 4 - Working with Data in Python

- Reading files with open
- Writing files with open
- Loading data with Pandas
- Working with and Saving data with Pandas

### Reading files with open 
```
# Download Example file

!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt
```
```
# Read the Example1.txt

example1 = "/resources/data/Example1.txt"
file1 = open(example1, "r")
```
```
# Print the path of file

file1.name
```
```
# Print the mode of file, either 'r' or 'w'

file1.mode
```
```
# Read the file

FileContent = file1.read()
FileContent
```
```
# Print the file with '\n' as a new line

print(FileContent)
```
```
# Type of file content

type(FileContent)
```
```
# Close file after finish

file1.close()
```
```
# Open file using with

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
```
```
# Verify if the file is closed

file1.closed
```
```
# See the content of file

print(FileContent)
```
```
# Read first four characters

with open(example1, "r") as file1:
    print(file1.read(4))
```
```
# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
```
```
# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))
```
```
# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())
```
```
# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1;
```
```
# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()
```
```
# Print the first line

FileasList[0]
```
```
# Print the second line

FileasList[1]
```
```
# Print the third line

FileasList[2]
```

### Writing files with open
```
# Write line to file

with open('/resources/data/Example2.txt', 'w') as writefile:
    writefile.write("This is line A")
```
```
# Read file

with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
```
```
# Write lines to file

with open('/resources/data/Example2.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
```
```
# Check whether write to file

with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
```
```
# Write a new line to text file

with open('/resources/data/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
```
```
# Verify if the new line is in the text file

with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
```
```
# Sample list of text

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
```
```
# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
```
```
# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
```
```
# Append the line to the file

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line D\n")
```
```
# Verify if the appending is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
```
```
# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
```
```
# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())
```

### Loading data with Pandas


### Working with and Saving data with Pandas