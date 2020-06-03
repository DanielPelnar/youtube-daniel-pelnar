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
# Chapter 9:
# Python Tutorial - core essentials: 9. Importing Modules and Standard Libraries

# Creating and importing our module:
import my_module

my_module.my_variable

z = my_module.my_variable

my_module.warning_function()
my_module.adding_two(20)

import my_module as m

m.my_variable

from my_module import adding_two

adding_two(4)

from my_module import *  # import all; not recommended

# OS 
import os

os.getcwd()
os.chdir('/Users/danielpelnar/')

# Math module:
    
import math 
math.exp(7)
math.log(10)
math.sqrt(4)

math.pi  # constants
math.e
math.inf

# Statistics module:
data = [23, 11, 2, 0, 101]
import statistics

statistics.mean(data)
statistics.median(data)
statistics.variance(data)

# Random module 
import random

random.randint(10, 20)
random.gauss(0, 1)

possible_names_of_unborn_son = ['James', 'John', 'Igor', 'Donald', 'Hua']

random.choice(possible_names_of_unborn_son)

random.shuffle(possible_names_of_unborn_son)

# Datetime module:

import datetime

now = datetime.date.today()
type(now)

first_day_2020 = datetime.date(2020, 1, 1)

difference = now - first_day_2020
difference.days


# Exercises:

# 1] What is infinite minus pi (use Math module):
# Solution:
import math
math.inf - math.pi

# 2] What is the median of the following series of numbers (use Statistics module):
x = [12, 12, 11, 33, 111]

# Solution:
import statistics
statistics.median(x)

    
# 3] How many days do we have until Christmas (use Datetime module):
# Solution:
import datetime
now = datetime.date.today()
ch = datetime.date(2020, 12, 24)
diff = ch - now
diff.days


# 4] You are very hungry but indifferent about what to eat for dinner.
# How would you choose randomly, with equal weights, what food to eat. (use Random module):
possible_dinner_choices = ["crabs balls", "chicken feet", "pigs brain", 
                           "ducks tongue", "pizza"]
# Solution:
import random
random.choice(possible_dinner_choices)


# 5] You realize that the only food that you can actually eat with open eyes is pizza.
# What is the probability of choosing pizza? hint: use method count() and function len() 

# Option 1:
prob = 1/5*100
# Option 2:
prob2 = possible_dinner_choices.count('pizza')/len(possible_dinner_choices)*100



