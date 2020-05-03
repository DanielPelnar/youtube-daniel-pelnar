### Python Tutorial: core essentials to program anything

### Chapters:
## 1. Variables and Strings - Assigning Values and Working with textual Data
## 2. Numeric Data Types - Working with integers and floats
## 3. Lists and tuples
## 4. Dictionaries
## 5. Set
## 6. If, Else, and Elif Statements
## 7. For Loops and While Loops
## 8. Functions
## 9. Classes

## Spyder editor is used throught the tutorial

## Structure of each video:
    # Explanation of syntax, commands and theory
    # Practical exercises with solutions to facilitate learning


# Chapter 1:
# Python Tutorial - core essentials: 1. Variables and Strings

# this is comment

# Strings
# '' or by ""
'We are so excited about learning python'  # This is a string
"Lets brainwash ourselves. I love Python. Say it 3x"
'a'
'eggs'

"""
text1
text2
text3

"""

'''
text1
text2
text3

'''

# Variables:

my_string = 'Wash hands'
my_string
print(my_string)



# Indexing and Slicing
#     W a s h   h a n d s
#     0 1 2 3 4 5 6 7 8 9    # positive indexing
#   -10-9-8-7-6-5-4-3-2-1    # negative indexing

my_string[0]
my_string[1]
my_string[2]
my_string[4]
my_string[-10]
my_string[-1]
my_string[15]

my_string[0:3]  # left side is included but the right side excluded.
my_string[0:4]
my_string[0:5]
my_string[0:10]

my_string[:4]
my_string[5:]
my_string[:]
my_string[0:10:2]
my_string[-5:-1]
my_string[1:-3]

my_string[::-1] # reverse string

# String methods:
x = ' Washing hands is important these days    '
x

x.upper()
g = x.upper()
g
x

g.lower()
x.count('a')
x.count('days')
x.find('g')
x.find('hands')
x.replace('these days', 'all the time')
x.title()
x.strip()


# Formating
'I want to buy {} apples and {} oranges'.format('super', 'rotten')

# Adding strings together and replication:

a = 'Python'
b = 'is'
c = 'amazing'

a + ' ' + b + ' ' + c

a*50


# Functions
len(x)

# Exercises
# 1] Get the 3rd word from string y and define the result as z:
y = 'dog and pandas are cute animals'
# Solution 1:
z = 'pandas'
# Solution 2:
z = y[8:14]
# Solution 3:
start = y.find('pandas')  # 8
pan_len = len('pandas')   # 6
end = start + pan_len     # 14
z = y[start:end]

# 2] Make the first letter of z upper case:
z.title()

# 3] Count how many 'a' are in the string z:
z.count('a')

# 4] Replace 'pandas' with 'unicorns' in string y:
y.replace('pandas', 'unicorns')
h = y.replace('pandas', 'unicorns')

# 5] How many characters does y contain?
len(y)

# 6] Reverse the string 'dog' using slicing:
'dog'[::-1]

my_var = 'dog'
my_var[::-1]










