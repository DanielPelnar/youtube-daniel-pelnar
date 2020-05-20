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
# Chapter 3:
# Python Tutorial - core essentials: 3. Lists and tuples

# Lists:
# A list stores a series of items in a particular order.
my_list = ['haha', 77, 77.3, 'anything']
type(my_list)
len(my_list) 

x = []
y = list()

# Basic statistics:
another_list = [2, 111, 0, 77, 342]
max(another_list)
min(another_list)
sum(another_list)

# Conditional testing:
'haha' in my_list
77 in my_list
'haha' not in my_list
'orange' in my_list

## Indexing and slicing of lists:
# Works the same as with strings
nice_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#             0    1    2    3    4    5    6    7    8    9      # positive indexing
#           -10   -9   -8   -7   -6   -5   -4   -3   -2   -1      # negative (reverse) indexing
# INDEXINGL nice_list[index]
# SLICING: nice_list[start:end:step]        # Left side inclusive; right side exclusive
nice_list[0]
nice_list[9]
nice_list[5]
nice_list[-5]

nice_list[0:4]
nice_list[4:6]
nice_list[:4]
nice_list[:]
nice_list[5:]

nice_list[0:10:3]
nice_list[0:10:2]
nice_list[::2]
nice_list[::-1]

# Adding lists together:
a = nice_list[0:6]
b = nice_list[6:10]
c = a + b

nice_list  == c

surname = ['Daniel'] + ['John'] + ['Harry', 'Clare']

surname * 3

# List methods:
animals = ['dog', 'cat', 'cow']
animals = animals + ['snake']
animals.append('snake')
animals.extend(['kiwi', 'whale'])
animals.insert(3, 'panda')
animals.sort()
animals.sort(reverse = True)
animals.index('snake')

# Joining: from list to string
''.join(animals)
' '.join(animals)
', '.join(animals)
d = 'X'.join(animals)

# Splitting: string to a list:
d.split('X')
d.split('a')

# Removing index:
del animals[-1]
del animals[0]

# Removing item:
animals.remove('panda')

# Popping items
colours = ['red', 'blue', 'green']
removed_item = colours.pop(1)

## Tuples
my_tuple = ('US', 'UK', 'Czechia', 'HK', 'China')
type(my_tuple)
my_tuple + ('Germany')

# Casting:
my_list = list(my_tuple)
my_list.append('Germany')

my_tuple = tuple(my_list)


# Exercises:
# 1] Add 2 elements: 'MERS' and 'Covid-19' to the following list:
pandemics = ['Spanish flu', 'HIV-AIDS', 'SARS', 'Swine flu', 'Ebola']
# Solution:
pandemics + ['MERS', 'Covid-19']

# Option 2:
pandemics.extend(['MERS', 'Covid-19'])

# Options 3:
pandemics.append('MERS')    
pandemics.append('Covid-19')

# Options 4:
pandemics.insert(0, 'MERS')
pandemics.insert(1, 'Covid-19')

# 2] Create an empty list called: empty_list
# Option 1:
empty_list = []
# Option 2:
empty_list = list()

# 3] Sort the following list alphabetically and delete item indexed 3:
pandemics = ['Spanish flu', 'HIV-AIDS', 'SARS', 'Swine flu', 'Ebola']
# Solution:
pandemics.sort()
del pandemics[3]

# 4] Is SARS in the following list? If so, delete it from the list:
pandemics = ['Spanish flu', 'HIV-AIDS', 'SARS', 'Swine flu', 'Ebola']
# Solution:
'SARS' in pandemics
pandemics.remove('SARS')

if 'SARS' in pandemics:
    pandemics.remove('SARS')

# 5] Create a string from the items in the following list. 
# The items in the string should be separated by the plus sign:
pandemics = ['Spanish flu', 'HIV-AIDS', 'SARS', 'Swine flu', 'Ebola']
# Solution:
'+'.join(pandemics)

# 6] Cast the following tuple into list and find the maximum:
num = (12, 1111, 21, 7432, 7432, 7431, 7333, 7322)
# Solution:
f = list(num)
max(f)
    
# 7] Using functions that we have learned, find the average of the numbers in the following list:
super_list = [12, 53, 33, 98, 28, 45, 12, 0, 20]
# Solution:
average = sum(super_list)/len(super_list)



