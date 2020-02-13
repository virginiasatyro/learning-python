# Python Basics for Data Science

## Module 2 - Python Data Structures

Learning Objectives

- Lists and Tuples 
- Sets
- Dictionaries 

### Lists and Tuples 

```
# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1
```
```
# Print the type of the tuple you created

type(tuple1)
```
```
# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
```
```
# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
```
```
# Use negative index to get the value of the last element

tuple1[-1]
```
```
# Use negative index to get the value of the second last element

tuple1[-2]
```
```
# Use negative index to get the value of the third last element

tuple1[-3]
```
```
# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2
```
```
# Slice from index 0 to index 2

tuple2[0:3]
```
```
# Slice from index 3 to index 4

tuple2[3:5]
```
```
# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
```
```
# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted
```
```
# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
```
```
# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])
```
```
# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])
```
```
# Print the first element in the second nested tuples

NestedT[2][1][0]
```
```
# Print the second element in the second nested tuples

NestedT[2][1][1]
```
```
# Print the first element in the second nested tuples

NestedT[4][1][0]
```
```
# Print the second element in the second nested tuples

NestedT[4][1][1]
```
```
# Create a list

L = ["Michael Jackson", 10.1, 1982]
L
```
```
# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )
```
```
# Sample List

["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
```
```
# Sample List

L = ["Michael Jackson", 10.1,1982,"MJ",1]
L
```
```
# List slicing

L[3:5]
```
```
# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L
```
```
# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L
```
```
# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L
```
```
# Use append to add elements to list

L.append(['a','b'])
L
```
```
# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
```
```
# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)
```
```
# Split the string, default is by space

'hard rock'.split()
```
```
# Split the string by comma

'A,B,C,D'.split(',')
```
```
# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A) # A: ["hard rock", 10, 1.2]
print('B:', B) # A: ["hard rock", 10, 1.2]
```
```
# Examine the copy by reference

print('B[0]:', B[0]) # B[0]: hard rock
A[0] = "banana"
print('B[0]:', B[0]) # B[0]: banana
```
```
# Clone (clone by value) the list A

B = A[:]
B # ['banana', 10, 1.2]

print('B[0]:', B[0]) # B[0]: banana
A[0] = "hard rock"
print('B[0]:', B[0]) # B[0]: banana
```

### Sets
```
# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1 # {'R&B', 'disco', 'hard rock', 'pop', 'rock', 'soul'}
```
```
# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982,  "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set # {'00:42:19', 10.0,1982,'30-Nov-82', 46.0, 65,'Michael Jackson', None, 'Pop, Rock, R&B', 'Thriller'}
```
```
# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", "progressive rock", "soft rock", "R&B", "disco"])
music_genres # {'R&B', 'disco', 'folk rock', 'hard rock','pop', 'progressive rock', 'rock', 'soft rock', 'soul'}
```
```
# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A # {'AC/DC', 'Back in Black', 'Thriller'}
```
```
# Add element to set

A.add("NSYNC")
A # {'AC/DC', 'Back in Black', 'NSYNC', 'Thriller'}
```
```
# Try to add duplicate element to the set

A.add("NSYNC")
A # {'AC/DC', 'Back in Black', 'NSYNC', 'Thriller'}
```
```
# Remove the element from set

A.remove("NSYNC")
A # {'AC/DC', 'Back in Black', 'Thriller'}
```
```
# Verify if the element is in the set

"AC/DC" in A # True
```
```
# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
```
```
# Print two sets

album_set1, album_set2
# ({'AC/DC', 'Back in Black', 'Thriller'}, {'AC/DC', 'Back in Black', 'The Dark Side of the Moon'})
```
```
# Find the intersections

intersection = album_set1 & album_set2
intersection # {'AC/DC', 'Back in Black'}
```
```
# Find the difference in set1 but not set2

album_set1.difference(album_set2)  # {'Thriller'}

album_set2.difference(album_set1)  # {'The Dark Side of the Moon'}
```
```
# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2) # {'AC/DC', 'Back in Black'}   
```
```
# Find the union of two sets

album_set1.union(album_set2) # {'AC/DC', 'Back in Black', 'The Dark Side of the Moon', 'Thriller'}
```
```
# Check if superset

set(album_set1).issuperset(album_set2) # False 
```
```
# Check if subset

set(album_set2).issubset(album_set1) # False 
```
```
# Check if subset

set({"Back in Black", "AC/DC"}).issubset(album_set1) # True
```
```
# Check if superset

album_set1.issuperset({"Back in Black", "AC/DC"}) # True 

A = [1, 2, 2, 1]  
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A)) # 6 
print("the sum of B is:", sum(B)) # 3
```

### Dictionaries 
```
# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict
```
```
# Access to the value by the key

Dict["key1"] # 1
```
```
# Access to the value by the key

Dict[(0, 1)] # 6
```
```
# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict
```
```
# Get value by keys

release_year_dict['Thriller'] # '1982'
```
```
# Get value by key

release_year_dict['The Bodyguard'] # '1992'
```
```
# Get all the keys in dictionary

release_year_dict.keys() # dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])
```
```
# Get all the values in dictionary

release_year_dict.values() # dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])
```
```
# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict # {'Thriller': '1982', 'Back in Black': '1980', 'The Dark Side of the Moon': '1973', 'The Bodyguard': '1992', 'Bat Out of Hell': '1977', 'Their Greatest Hits (1971-1975)': '1976', 'Saturday Night Fever': '1977', 'Rumours': '1977', 'Graduation': '2007'}
```
```
# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict # {'Back in Black': '1980', 'The Dark Side of the Moon': '1973', 'The Bodyguard': '1992', 'Bat Out of Hell': '1977', 'Their Greatest Hits (1971-1975)': '1976', 'Saturday Night Fever': '1977', 'Rumours': '1977'}
```
```
# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict # True
```