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
# Chapter 4:
# Python Tutorial - core essentials: 4. Dictionaries

# Dictionaries
# Each item is a key-value pair.
my_dict = {'name': 'Daniel', 
           'colours': ['red', 'green', 'yellow'], 
           'numbers': (23, 12, 43), 
           73: 'haha'}

my_dict.keys()
my_dict.values()

# Acessing a value:
my_dict['name']
my_dict['colours']
my_dict[73]
my_dict['colours'][1]

# Updating values:
my_dict['name'] = 'James'
my_dict['colours'][2] = 'black'

# Adding a new key and value:
my_dict['age'] = 100
my_dict.update({'food': ['banana', 'apple'], 'movie': 'Big Short'})

# Removing items from our dict:
del my_dict['food']

# Popping items from our dict:
popped_item = my_dict.pop('movie')


## Exercises:
# 1] Create an empty dictionary:
# Option 1:
x = {}
# Option 2:
y = dict()

# 2] Add a key-value pair, where 'countries' is the key and 'Spain' is the value:
# Solution:
x['countries'] = 'Spain'

# 3] From the following dictionary, access 'lobster'
x = {'drinks': ['Cola', 'Fanta'], 'food': ['hotdog', 'apple', 'lobster']}
# Solution:
x['food'][2]

# 4] From the following dictionary, access 'w' from 'water'
y = {'name': 'Peter', 'food': 'banana', 'drink': ['water']}
# Solution:
y['drink'][0][0]

# 5] Add Cola and Sprite to drink 
# so that the key is 'drink' and value is a list of water, Cola and Sprite:
# Solution:
y = {'name': 'Peter', 'food': 'banana', 'drink': ['water']}
y['drink'].extend(['Cola', 'Sprite'])


