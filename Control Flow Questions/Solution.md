## Question 
Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

## Solution 
```python
result = []
for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)
print(result)
```
## Question 2
Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius

```python

celsius = int(input("Enter Celsius: "))
fahrenheit= int(input("Enter Fahrenheit: "))

# Application of the formular
formularCelsius = (celsius * 9/5) + 32
formularFahrenheit = (fahrenheit - 32) * 5/9
print(f"{celsius}°C is {int(formularCelsius)} in Fahrenheit")
print(f"{fahrenheit}°F is {int(formularFahrenheit)} in Celsius")

```

## Question 3
Write a Python program to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

## Solution 
```python
import random
tryGuess = random.randint(1,9)
while True:
    guess = int(input("Guess a number between 1 and 9: "))
    if tryGuess == guess:
        print("Gessed right!")
        break
```

## Question 4
Write a Python program that accepts a word from the user and reverses it.

## Solution 

```python 
word = input("Please Enter word ")
reversedWord = word[::-1]
print("The reversed words are:",reversedWord)
```

## Question 5
Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :
Number of even numbers : 5
Number of odd numbers : 4

## Solution
```python
## Question 5
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
evenNum = 0
oddNum = 0
for number in numbers:
    if number % 2 == 0:
        evenNum += 1
    else:
        oddNum += 1     
        
print("The even nummbers are:",evenNum)
print("The odd nummbers are:",oddNum)

```
## Question 6 
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

Note : Use 'continue' statement.

Expected Output : 0 1 2 4 5

## Solution 
```python
for num in range(0, 6):
    if num == 3:
        continue
    print(num, end=" ")

```

## Question 7
Write a Python program to get the Fibonacci series between 0 and 50.

Note : The Fibonacci Sequence is the series of numbers :

0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.

Expected Output : 1 1 2 3 5 8 13 21 34

## Solution
```python
a, b = 0, 1

while b < 50:   # continue until b reaches 50
    print(b, end=" ")
    a, b = b, a + b

```

## Question 8
Write a Python program to construct the following pattern, using a nested for loop.

## Solution 
```python
num = int(input("Please enter a number: "))
for i in  range(num):
    for j in range(i + 1):
        print("*", end=" ")
    print()
    
for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()
```
## Question
Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

Sample Output :

fizzbuzz
1
2
fizz
4
buzz
## Solution
```python
for i in range(1, 50 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    else:
        print(i)
```
## Question 
Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

## Solution
```python
rows = int(input("Enter a number: "))
cols = int(input("Enter a number: "))

result = []
for i in range(rows):
    rows = []
    for j in range(cols):
        rows.append(i * j)
    result.append(rows)
print(result)
``` 
## Question 
Write a Python program that accepts a string and calculates the number of digits and letters.

Sample Data : Python 3.2

Expected Output :

Letters 6
Digits

## Solution
```python
s = input("Input a string")

# Initialize variables 'd' (for counting digits) and 'l' (for counting letters) with values 0
d = 0
l = 0

# Iterate through each character 'c' in the input string 's'
for c in s:
    # Check if the current character 'c' is a digit
    if c.isdigit():
        # If 'c' is a digit, increment the count of digits ('d')
        d = d + 1
    # Check if the current character 'c' is an alphabet letter
    elif c.isalpha():
        # If 'c' is an alphabet letter, increment the count of letters ('l')
        l = l + 1
    else:
        # If 'c' is neither a digit nor an alphabet letter, do nothing ('pass')
        pass

# Print the total count of letters ('l') and digits ('d') in the input string 's'
print("Letters", l)
print("Digits", d)
```

## Question 
Write a Python program to check the validity of passwords input by users.

Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

## Solution
```python
while True:
    password = input("Please Enter password: ")

    # Conditions
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "$#@" for c in password)
    valid_length = 6 <= len(password) <= 16

    if has_lower and has_upper and has_digit and has_symbol and valid_length:
        print("✅ Password Accepted")
        break
    else:
        print("❌ Invalid password. Try again!")
```

## Question 
Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

## Solution
```python
# Create an empty list named 'items'
items = []

# Iterate through numbers from 100 to 400 (inclusive) using the range function
for i in range(100, 401):
    # Convert the current number 'i' to a string and store it in the variable 's'
    s = str(i)
    
    # Check if each digit in the current number 'i' is even (divisible by 2)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        # If all digits are even, append the string representation of 'i' to the 'items' list
        items.append(s)

# Join the elements in the 'items' list separated by ',' and print the result
print(",".join(items)) 
```

## Question
Write a Python program to check whether an alphabet is a vowel or consonant.

Expected Output:

Input a letter of the alphabet: k    

## Solution
```python
word = input("Please enter a word: ")
vowel = 'a', 'e', 'i', 'o', 'u'

for letter in word:
    if letter in vowel:
        print(f"{letter} is a vowel" )
    else:
        print(f"{letter} is not a consonant")
```

## Question 
Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
```python 
# Define a function named 'sum' that takes two parameters 'x' and 'y'
def sum(x, y):
    # Calculate the sum of 'x' and 'y' and assign it to the variable 'sum'
    sum = x + y
    
    # Check if the calculated sum falls within the range of 15 to 19 (inclusive)
    if sum in range(15, 20):
        return 20  # If the sum falls within the specified range, return 20
    else:
        return sum  # If the sum doesn't fall within the specified range, return the calculated sum

# Call the 'sum' function with different arguments and print the results
print(sum(10, 6))   # Call the function 'sum' with arguments 10 and 6, then print the result
print(sum(10, 2))   # Call the function 'sum' with arguments 10 and 2, then print the result
print(sum(10, 12))  # Call the function 'sum' with arguments 10 and 12, then print the result 

```

## Question
Write a Python program that checks whether a string represents an integer or not.

Expected Output:

Input a string: Python                                                  
The string is not an integer.

## Solution 
```python 
numWord = input("Enter your word: ")
if numWord.isdigit() or numWord.startswith("-") and numWord[1::].isdigit() :
    print("The string is an integer")
else:
    print("The string is not an integer")

# Alternatively
try:
    int(numWord)
    print("The string is an integer")
except ValueError:
    print("The string is not an integer")
```

## Question 
Write a Python program to check if a triangle is equilateral, isosceles or scalene.

Note :

An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.

Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle  

## Solution
```python
sideX = int(input("Enter side X: "))
sideY = int(input("Enter side Y: "))
sideZ = int(input("Enter side Z: "))

if sideX == sideY == sideZ:
    print("This ia an An equilateral triangle")
elif sideX != sideY and sideY != sideZ and sideX != sideZ:
    print("This ia an Scalene triangle")
else:
    print("This ia an Isosceles triangle")

    # Alternative
sides = {sideX, sideY, sideZ}

if len(sides) == 1:
    print("Equilateral")
elif len(sides) == 2:
    print("Isosceles")
else:
    print("Scalene")
```

## Question 
Write a Python program to find the median of three values.

Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0  