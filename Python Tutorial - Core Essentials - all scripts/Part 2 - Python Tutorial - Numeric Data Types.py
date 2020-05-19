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

## Spyder editor is used throught the tutorial. 
# To run selected code or current line:
    # In the Tool menu (on the top of the screen), click on 'Run' and then click on 'Run selection or current line'
    # Mac shortcut: COMNAND ENTER
    # Windows shortcut: F9

## Structure of each video:
    # Explanation of syntax, commands and theory
    # Practical exercises with solutions to facilitate learning

### In this video:
# Chapter 2:
# Python Tutorial - core essentials: 2. Numeric Data Types - Working with integers and floats

# Strings vs Integers vs Floats:
    
z = '7'
type(z)
v = '7.3'
type(v)
y = 7  # Integer
type(y)
w = 7.3
type(w) # floats

# Casting:

type(int(z))
float(v)
str(y)
type(int(w))

# Python as a calculater:

3 + 2

2 - 1

14 / 3

14 // 3   # floor division

14 % 3    # remainder

2**4      # using double **


# Incrementing variables

num = 3
num = num + 2

num = 3
num += 2

num = 4
num = num * 2

num = 4
num *= 2

num = 8
num = num / 2

num = 8
num /= 2

# Comparisons
a = 21
b = 3

a == b
a != b

a > b
a >= b

a < b
a <= b

# Built-in Python functions 

abs(-30)
abs(4500)

round(30.749)
round(30.749, 2)
round(30.749, 1)

# Math module
import math

math.exp(7)
math.log(10)
math.sqrt(4)

math.pi
math.e
math.inf
-math.inf



# Exercises:
# 1] What is the remainder of 345 divided by 17
# Solution:
345 % 17

# 2] Is 478 an even number ? 
# Solution:
num = 478 % 2
num == 0


# 3] Cast the following string into float:
x = '9.63'
# Solution:
float(x)

# 4] Cast the following integer into string and check that you actually got a string:
y = 111
# Solution:
type(str(y))

# 5] Increment the following number by 200:
n = 7
# Option 1:
n = n + 200
# Option 2:
n = 7
n += 200


# 6] Using Math Module. What is e^11? Round the result to two decimal places:
# Solution: 
import math
x = math.exp(11)
y = round(x, 2)
y

# 7] Use Math module to find out the result of log(e):    (e represents Euler's number and log() represents natural log)
# Solution:
a = math.e
math.log(a)


# 8] What is the output of '2'+'2' and what is the output of 2 + 2
# Solution:
'2' + '2'
2 + 2

'Daniel' 
'Pelnar'
'Daniel' + 'Pelnar'







