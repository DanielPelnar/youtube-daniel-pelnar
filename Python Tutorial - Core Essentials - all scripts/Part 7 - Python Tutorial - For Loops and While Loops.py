###  Python Tutorial - core essentials

### Chapters:
## 1. Variables and Strings - Assigning Values and Working with textual Data
## 2. Numeric Data Types - Working with integers and floats
## 3. Lists and tuples
## 4. Dictionaries
## 5. Set
## 6. If, Else, and Elif Statements
## 7. For Loops and While Loops
## 8. Functions
## 9. Importing Modules and Standard Libraries

## Spyder editor is used throughout the tutorial. 
# To run selected code or current line:
    # In the Tool menu (on the top of the screen), click on 'Run' and then click on 'Run selection or current line'
    # Mac shortcut: COMNAND ENTER
    # Windows shortcut: F9

## Structure of each video:
    # Explanation of syntax, commands and theory
    # Practical exercises with solutions to facilitate learning

### In this video:
# Chapter 7:
# Python Tutorial - core essentials: 7. For Loops and While Loops

## For Loops and While Loops

# For Loops:
# A few examples of For Loops with lists:
my_list = ['air', 'tree', 'water', 'stone']

for item in my_list: # item is arbitrary - can be literally anything; see below:
    print(item)
    
for anything in my_list:
    print(anything)
    
# Example 2:
new_list = []
    
for i in my_list:
    x = i.title()
    new_list.append(x)

# Example 3:
numbers = [3, 1, 7, 9, 11]

numbers2 = []

for number in numbers:
    a = number * 2
    numbers2.append(a)
    
# Else:
numbers = [1,2,3,4]

for num in numbers:
    print(num)
else:
    print('The For loop has finished')
    
# Enumerate:
random_list = ['a', 'b', 'c', 'd']

for index, item in enumerate(random_list):   
    print(index)
    print(item)
    
for index, item in enumerate(random_list, start = 10):
    print(index, item)
    
x = enumerate(random_list)
type(x)
list(x)

# Range:
x = range(10)
type(x)
list(x)

for i in range(10):
    print(i)
    
for i in range(5, 20):
    print(i)
    
for i in range(5, 20, 2):
    print(i)

# Pass:
for integer in range(5):
    pass

# Iterating over items in tuples:
my_tuple = ['x', 'y', 'z']

for item in my_tuple:
    print(item)
    
# Iterating over keys and values in dictionaries:
my_info = {'name': 'Daniel', 'surname': 'Pelnar', 'age': 26}

for key in my_info:
    print(key)
    
for value in my_info.values():
    print(value)
    
for key, value in my_info.items():
    print(key, value)
    
for x, y in my_info.items():
    print(x, y)
    
# Iteration over characters in strings:
my_string = 'After coming back home, you better wash hands!'

for character in my_string:
    print(character)


new_string = 'abc'
new_list = []

for char in new_string:
    x = char.upper()
    new_list.append(x)
    
# Break and Continue:
numbers = [1,2,3,4,5]
numbers = range(1,6)
numbers = list(numbers)

for i in numbers:
    print(i)

for i in numbers:
    print(i)
    break

for i in numbers:
    if i == 3:
        break
    print(i)

# Break is used for stopping the loop before it has finishes.
# Continue is used for skipping the rest of the loop.

for num in numbers:
    if num == 3:
        continue
    print(num)

# Nested Loops:
numbers = [1,2,3]
items = ['A', 'B']

for number in numbers:
    for item in items:
        print(number, item)
        
# While Loops:
# While loops iterate as long as a certain condition is True.
x = 0

while x <= 4:   # infinite while loop
    print(x)
    
while x <= 4: 
    print(x)
    x += 1

# Removing 'Nan' using while loop:    
my_list = ['a', 'b', 'Nan', 'Nan', 'c', 'Nan']

while 'Nan' in my_list:
    my_list.remove('Nan')

## Comprehensions
# List comprehension:
numbers = [3, 1, 7, 9, 11]
numbers2 = []

for number in numbers: 
    a = number * 2
    numbers2.append(a)
    
numbers_doubled = [number * 2 for number in numbers]  # list comprehension

# Set comprehension:
b = {'abc', 'def'}
b_2 = {i.upper() for i in b}

# Dict comprehension:
c = {'number1': 3, 'number2': 2}
c_2 = {k:v+1 for k,v in c.items()}


## Exercises:
# 1] Create a For Loop which prints the following integers: 
# 0, 2, 4, 6, 8: (hint: use 'range')
# Solution:
for i in range(0,10,2):
    print(i)

# 2] Capitalize the first letter and 
# print each item from the following list using For Loop:
animals = ['whale', 'cat', 'ant']
# Solution:
for animal in animals:
    print(animal.title())


# 3] Create an empty list and use method append to populate it with
# items from string_numbers. 
# Before you populate the the empty list, cast those items into integers:
string_numbers = ['23', '11', '1', '78', '2']
# Solution:
empty_list = []
for item in string_numbers:
    empty_list.append(int(item))

    
# 4] Use While Loop to delete all empty strings from the following list:
x = ['Python', ' ', ' ', 'R', 'Java', ' ', 'SQL']
# Solution:
while ' ' in x:
    x.remove(' ')


# 5] Consider the following dictionary. Using 'comprehension' to switch keys with values:
c = {'name': 'John', 'age': 5}
# Solution:
c_2 = {v:k for k,v in c.items()}

# 6] Consider the following For Loop. How would you write it using 'comprehension':
b = ['AAA','BBB','CCC']
b_2 = []
for item in b:
    b_2.append(item.lower())
# Solution:
b_3 = [item.lower() for item in b]

# 7] (challenging) Consider the following For Loop. 
# How would you write it using 'comprehension':
numbers = range(10)
my_list1 = []

for num in numbers:
    if num < 6:
        my_list1.append(num)
# Solution:        
my_list2 = [num for num in numbers if num < 6]


        


