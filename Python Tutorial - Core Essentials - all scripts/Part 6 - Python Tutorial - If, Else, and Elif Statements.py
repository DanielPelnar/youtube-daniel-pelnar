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
# Chapter 6:
# Python Tutorial - core essentials: 6. If, Else, and Elif Statements


## Building blocks:
# If statements test for a particular condition and respond based on the result.

## Comparison Operators:
# Equal:                           ==
# Not Equal:                       !=
# Greater or equal:                >=
# Less than:                       <
# Identity operation:              is    (checking for same object in memory)

## Logical Operators:
# Both have to be True:            and
# At least one has to be True:     or
# Reverse logical operator:        not

## These values Python evaluates as False. By default, anything else is True:
# False
# None
# Zero of any numerical type
# Any empty sequence. For example '' () []
# Any empty mapping. For example {}
# Check it yourself using function: bool()

# If Statements:
if 4 > 10:
    print('4 is larger than 3')
    

# If and Else Statement:
    
if 1100 > 100:
    print('Message')
else:
    print('Something')

# Elif:
I_want = 'mango'  # apple, mango
shopping_list = []

if I_want == 'banana':
    shopping_list.append(I_want)
elif I_want == 'apple':
    shopping_list.append(I_want)
else:
    print('I am gonna be hungry')

# Example 2 (Logical operator: and)

bank_balance = 0.5
number_infected = 1000  

if (bank_balance >= 1 and number_infected < 100):
    print('I can go outside to drink beer')
elif (bank_balance < 1 and number_infected < 100):
    print('I can go outside but I am broke.')
elif (bank_balance >= 1 and number_infected > 100):
    print('I have enough money but it is dangerous to go outside')
elif (bank_balance < 1 and number_infected > 100):
    print('I am broke but I cant go outside anyway.')

# Example 3 (logical operator: or)
age = 11
friend = False

if (age >= 18 or friend):
    print('I can get a beer')
else:
    print('I am out of luck.')

# Example 4 (logical operator: not):
    recession = False 

if not recession:
    print('There are plenty of jobs')
else:
    print('No jobs')
    
# Example 5:
value = 'some string'

if value:
    print('This is evaluated by Python as True')
else:
    print('This is evaluated by Python as False')
    
   

# Exercises:
# 1] Is the following statement True or False? 
# Can you tell without first running the code:
((30 <= 25 or 10 == 10) and not(False))

# 2] Is the following statement True or False? 
# Can you tell without first running the code:
x = 20
y = 5
not(not(x >= 10 or x < 3) and y < x)

# 3] Write an If, Else statement which prints: 'I have a dog' if variable dog = True, 
# and prints: I dont have a dog if variable dog = False
dog = False
# Solution:
if dog:
    print('I have a dog')
else:
    print('I dont have a dog')


# 4] Replace X inside the code with one of the following arithmetic operators (+ - * ** / %) 
# so that the If statement holds for any positive integer: 

value = 47

if (value % 2) == 0:
    print('This is an even number')
else:
    print('This is an odd number')
    
    
# 5] Write If statement which deletes 'water' from the following list
# under the condition that 'water' is in the list:
food = ['pizza', 'chips', 'ham', 'water', 'apple']
# Solution:
if 'water' in food:
    food.remove('water')
    

    

    





