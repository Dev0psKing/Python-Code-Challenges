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