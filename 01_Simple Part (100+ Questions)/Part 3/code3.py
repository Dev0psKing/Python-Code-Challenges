# 400+ Python Solved Problems from Beginner to Advanced.

# Question 1

# Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0 and
# 1.0, print a grade using the following table:


# Grade | Score |
# --- | --- |
# A | >= 0.9 |
# B | >= 0.8 |
# C | >= 0.7 |
# D | >= 0.6 |
# F | < 0.6 |

# Solution

print('HELLO WELCOME TO SCORE YOUR CHECKER ')

try:
    score = float(input('What did you score between 0.0 - 1.0?: '))
except ValueError:
    print("Bad Score")
    quit()

if score > 0.9:
    print('Bad Score')
elif score >= 0.9:
    print("Your grade is A")
elif score >= 0.8:
    print("Your grade is B")
elif score >= 0.7:
    print("Your grade is C")
elif score >= 0.6:
    print("Your grade is D")
else:
    print("Your grade is F")


# Question 2

# Write a Python function called longest_word that takes three input strings as arguments: word1, word2, and word3. The function should determine and return the longest word among the three input words. Use the logic demonstrated in the following examples:
#
#
# print(longest_word("chair", "couch", "table"))   # Output should be: "chair"
# print(longest_word("bed", "bath", "beyond"))     # Output should be: "beyond"
# print(longest_word("laptop", "notebook", "desktop"))  # Output should be: "notebook"
#
# Your function should be able to correctly identify the longest word among the input strings and return it as the output.


# Soution

def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return word


print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

# Output

# chair
# beyond
# notebook

# Question 3

# Write a program to test the compatibility between two people.
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores **less than 10** or **greater than 85**, the message should be:

# `"Your score is **x**, you go together like coke and mentos."`

# For Love Scores **between 40** and **70**, the message should be:

# `"Your score is **y**, you are alright together."`

# Otherwise, the message will just be their score. e.g.:
#
# `"Your score is **z**."`

# Example

# `name1 = "David"`

# `name2 = "Jennifer"`

# T occurs 0 times

# R occurs 1 time

# U occurs 0 times

# E occurs 2 times

# Total = 3

# L occurs 0 time
#
# O occurs 0 times

# V occurs 1 times

# E occurs 2 times

# Total = 3

# Love Score = 33

# Print: "Your score is 33."

# # Example Input 1

# ```
# name1 = "David"
# ```

# ```
# name2 = "Jennifer"
# ```

# # Example Output 1

# ```
# Your score is 33.
# ```

#  Hint

# 1. The `lower()` function changes all the letters in a string to lower case.

# 2. The `count()` function will give you the number of times a letter occurs in a string.

# Solution
import random

print('Welcome to Love Calculator ')
name1 = input('What is your name? ')
name2 = input('What is the name of your lover? ')

lowerCaseNAme = name1.lower() + name2.lower()
# print(lowerCaseNAme)

matchedScores = random.randint(0, 100)

if matchedScores < 10 or matchedScores > 85:
    print(f"Your score is {matchedScores}, you go together like coke and mentos.")
elif matchedScores == 40 or matchedScores <= 70:
    print(f"Your score is {matchedScores}, you are alright together.")
else:
    print(f"Your score is {matchedScores}:")

# Another way of solving this is using strings to concatinate it. but the first way is the best since its a game program.

print('Welcome to Love Calculator ')
name1 = input('What is your name? ')
name2 = input('What is the name of your lover? ')

lowerCaseNAme = name1.lower() + name2.lower()
# print(lowerCaseNAme)

t = lowerCaseNAme.count('t')
r = lowerCaseNAme.count('r')
u = lowerCaseNAme.count('u')
e = lowerCaseNAme.count('e')
true = t + r + u + e

l = lowerCaseNAme.count('l')
o = lowerCaseNAme.count('o')
v = lowerCaseNAme.count('v')
e = lowerCaseNAme.count('e')
love = l + o + v + e

matchedScores = int(str(true) + str(love))

if matchedScores < 10 or matchedScores > 85:
    print(f"Your score is {matchedScores}, you go together like coke and mentos.")
elif matchedScores == 40 and matchedScores <= 70:
    print(f"Your score is {matchedScores}, you are alright together.")
else:
    print(f"Your score is {matchedScores}:")


# Question 4

# write a program to show such type of layouts of numbers, squares, and cube.

# Expected Output:

# Number    Square   Cube
# 1         1        1
# 2         4        8
# 3         9        27
# 4         16       64
# 5         25       125

# Solution

print('Number \t\t Square \t\t  Cube')
print(f'{1}\t\t \t {1**2} \t\t \t\t  {1**3}')
print(f'{2}\t\t \t {2**2} \t\t \t\t  {2**3}')
print(f'{3}\t\t \t {3**2} \t\t \t\t  {3**3}')
print(f'{4}\t\t \t {4**2} \t \t\t  {4**3}')
print(f'{5}\t\t \t {5**2} \t \t\t  {5**3}')

# Using loops to solve this question they will both give same answer.

print('Number\tSquare\tCube')
for i in range(1, 6):
    print(f'{i}\t\t{i**2}\t\t{i**3}')


# Question 5

# Write a program that displays name and age of users.

# Solution

print('Hello User!')
name = input('What is your name?: ')
age = input("How old are you?: ")

print(f'Hi {name}! Your age is {age}')


## Question 7

# Write a program that performs all arithmetic operations (addition, subtraction, multiplication, division) on two variables provided by the user.

#Solution

first_number = int(input('Enter your first number: '))
second_number = int(input('Enter your second number: '))

print(f'sum:= {first_number + second_number} ')
print(f'sum:= {first_number - second_number} ')
print(f'sum:= {first_number * second_number} ')
print(f'sum:= {first_number / second_number} ')

# Question 8

# Write strings on the python interactive shell. The strings are the following:
#
# * Your name
# * Your Surname
# * Your country
# * I am Crushing Python Questions

# Solution

# Using multiple variable assignment

name, surname, country, fact = 'Collins', 'Uwabor', 'Nigeria', 'I am Crushing Python Questions.'

print('My name is', name, surname, 'from', country, 'and', fact)


## Question 9

# Write a Python program that calculates the intersection of two sets. Set A and Set B are provided as input,
# and the program should find the union of these two sets.

# Solution

# Steps/ Algorithm to solve this.
# N.B: Know that you can use & methods or intersection() function to solve this.

# Receive sets as strings and split them into elements
setA = input('Enter your first set (e.g. 3, 2, 4, 5, 6, 7, 8): ')
setB = input('Enter your second set (e.g. 4, 12, 5, 1, 6, 8): ')

# Split the input strings into elements using commas as separators
setA_elements = setA.split(',')
setB_elements = setB.split(',')

# Create sets from the elements
setA = set(map(int, setA_elements))
setB = set(map(int, setB_elements))

setC = setA & setB

print("Intersection of Set A and Set B:", setC)

# Alternatively
setC = setA.intersection(setB)

print("Intersection of Set A and Set B:", setC)


# Question 10

# Write a Python program that calculates the difference of two sets. Set A and Set B are provided as
# input, and the program should find the union of these two sets.

# Solution


# Steps/ Algorithm to solve this.
# N.B: Know that you can use -= methods or difference() function to solve this.

# Receive sets as strings and split them into elements
setA = input('Enter your first set (e.g. 3, 2, 4, 5, 6, 7, 8): ')
setB = input('Enter your second set (e.g. 4, 12, 5, 1, 6, 8): ')

# Split the input strings into elements using commas as separators
setA_elements = setA.split(',')
setB_elements = setB.split(',')

# Create sets from the elements
setA = set(map(int, setA_elements))
setB = set(map(int, setB_elements))

setC = setA.difference(setB)

print("difference of Set A and Set B:", setC)

# Alternatively
setA -= setB

print("difference  of Set A and Set B:", setA)

