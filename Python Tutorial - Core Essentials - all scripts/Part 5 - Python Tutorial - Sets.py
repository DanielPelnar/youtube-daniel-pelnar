###  Python Tutorial - core essentials

### Chapters:
## 1. Variables and Strings - Assigning Values and Working with textual Data
## 2. Numeric Data Types - Working with integers and floats
## 3. Lists and tuples
## 4. Dictionaries
## 5. Sets
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
# Chapter 5:
# Python Tutorial - core essentials: 5. Sets

## Sets:    
fruits = {'grapefruit', 'apple', 'banana', 'apple', 'tomatoe', 'orange'} # sets are unordered and they don't have duplicates.
type(fruits)
empty_set = set()  # We can't use just {}
g = {}
type(g)
type(empty_set)

# Conditions for sets:
'apple' in fruits
'mango' not in fruits
'avocado' in fruits

# Set methods:
food = {'salmon', 'banana', 'potatoe', 'orange'}
food.add('pizza')
food.update(['chips', 'pasta'])
food.remove('banana')

x = food.union(fruits)
y = food.intersection(fruits)
f = food.difference(fruits)

# Casting sets into list and tuples; back:
my_list = list(food)
my_set = set(my_list)
my_tuple = tuple(my_set)


## Exercises:
# 1] Create an empty set and assigned it to an variable my_courses:
# Solution:
my_courses = set()

# 2] Add the following items to my_courses: 
# 'Math', 'Computer Science', 'Physics', 'Biology', 'Holiday'
# Solution:
my_courses.update(['Math', 'Computer Science', 'Physics', 'Biology', 'Holiday'])

# 3] In retrospect, you realized that 'Holiday' is actually not a course as much as 
# you would like it to be. Get rid of 'Holiday' from the set:
# Solution:
my_courses.remove('Holiday')

# 4] You want to find out what courses you share with your friend. 
# What method would you use?
your_friends_courses = {'Chemistry', 'Math', 'Data Science'}
# Solution:
your_friends_courses.intersection(my_courses)

# 5] You are super excited that you share one course with your friend. 
# Using Conditions, how would you double check that the course is really in your courses?
# Solution:
'Math' in my_courses

# 6] You really want to have only unique values in the following list. 
# How would you get rid of duplicates?
new_list = ['grass', 'sun', 'grass', 'tree', 'storm', 'water', 'water']
# Solution:
a = set(new_list)
new_list = list(a)






