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
guess = int(input("Guess a number between 1 and 9: "))
tryGuess = random.randint(1,9)

while tryGuess != guess:
    guess = int(input("Guess a number between 1 and 9: "))

else:
    print("Well guessed!")

```

## Question 4
Write a Python program that accepts a word from the user and reverses it.

## Solution 

```python 
word = input("Please Enter word ")
reversedWord = word[::-1]
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
        
print(evenNum)
print(oddNum)

```
