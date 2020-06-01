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
# Chapter 8:
# Python Tutorial - core essentials: 8. Functions


# Functions without any argument:
def warning_function():
    '''
    Documentation:
    Does not take any input.
    Outputs a string
    '''
    return 'Wash Hands!'

warning_function()
help(warning_function)
type(warning_function)
type(warning_function())
warning_function().upper()

# Functions with one input:    
def adding_two(value):
    '''
    Documentation:
    Inputs a number.
    Outputs the number + 2
    '''
    return value + 2

adding_two(10)
type(adding_two(10))
adding_two(10) + 10
str(adding_two(10)) + ' is a number'

def mult_fce(x, y):
    return x * y

mult_fce(10, 5)

# Functions that take a list as an argument:    
countries = ['uk', 'canada', 'vietnam', 'india', 'czechia']

def upper_cased(z):
    
    y = []
    
    for country in z:
        y.append(country.title())
    
    return y

upper_cased(countries)

# Positional arguments vs Keyword arguments:   
def lunch(drink, food):
    return 'I will drink {} and I will eat {}'.format(drink, food)

lunch('Cola', 'pasta') 
lunch('pasta', 'Cola')

lunch(drink = 'Cola', food = 'pasta')
lunch(food = 'pasta', drink = 'Cola')

# Functions with default arguments:   
def fav_colour(y = 'green'):
    return 'My fav colour is {}'.format(y)

fav_colour()
fav_colour('red')

## Passing an arbitrary number of arguments:
# Sometimes you won't know how many arguments a
# function will need to accept. Python allows you to collect an
# arbitrary number of arguments into one parameter using the
# * operator. A parameter that accepts an arbitrary number of
# arguments must come last in the function definition.
# The ** operator allows a parameter to collect an arbitrary
# number of keyword arguments.
# The * operator allows a parameter to collect an arbitrary
# number of positional arguments.

# We use *args when we have indefinite number of positional arguments:

def favourite_fruit(*args):
    for fruit in args:
        print(fruit)
        
favourite_fruit('banana', 'apple', 'mango')

def favourite_fruit(*fruits):  # args is arbitrary; * packs all the positional arguments  into a tuple.
    for fruit in fruits:
        print(fruit)
        
favourite_fruit('banana', 'apple', 'mango')

# We use **kwargs when we have indefinite number of keyword arguments:
    
def properties_fruit(**kwargs): 
    for x,y in kwargs.items():
        print(x,y)
        
properties_fruit(colour = 'red', weight = '10g', shape = 'square')

def lunch(food, *people):
    print(food, people)
    
lunch('banana', 'John', 'Marty', 'Daniel')  
lunch('chicken', 'Daniel')                  
lunch('fish')    

def super_lunch(food, **people):
    print(food, people)
    
super_lunch('pork', brother = 'Martin', father = 'Jiri') 
super_lunch('pork') 


# Exercises:
# 1] What will the following function return:
def fce1():
    return '1'+'1'

# Solution:
fce1()

# 2] What will the following function return:
def fce2():
    return 1+1

# Solution:
fce2()
    
# 3] Use the output of fce2 as an argument/input for fce3 and find out what fce3 outputs:
def fce3(x):
    z = 5 * x
    return z

# Solution:
fce3(fce2())

# 4] Complete the following lines of code so it does not output an error:
def pet(x):
    return 'I would really like to own {}'.format(x)

pet('dog')

# 5] Create a function called is_even(x) 
# which returns True if the input is an even number and false otherwise:

# Solution:
def is_even(x):
    
    if x % 2 == 0:
        return True
    else:
        return False

is_even(2341)
is_even(4)






