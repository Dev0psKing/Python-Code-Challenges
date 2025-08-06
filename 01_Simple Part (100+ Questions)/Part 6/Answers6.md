# 400+ Python Solved Problems from Beginner to Advanced.

## Question 1
Implement a function which takes a given ordered list as a parameter and displays numbers divisible by 5 and if a number is greater than 130 display STOP in the console.

### Example
list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200] 
numbers_divisible_by five(list1)

### Output:
~~~
15
40
75
STOP
~~~

```python
# Solution

def numbers_divisible_byfive(p_list):
    for i in p_list:
        if i >= 130:
            break
        if i % 5 == 0:
            print(i)
    print('STOP')
    
numbers_divisible_byfive([12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200])

# Alternatively:
# Solution 2

def numbers_divisible_byfive(p_list):
    total = 0 
    for i in p_list:
        if i % 5 == 0:
            print(i)
            total += i 
            if total >= 130:
                break 
    print('STOP')
    
numbers_divisible_byfive([12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200])
```


## Question 2
Implement a function that takes an integer number as a parameter and returns factorial of this number.
Factorial Equation (!)
5! = 5 x 4 x 3 x 2 x 1 = 120
4! = 4 x 3 x 2 x 1 = 24
If input is 0 then the return value will be: The factorial of 0 is 1
if input is a negative number then the return value will be: Factorial does not exist for negative numbers

### Example
~~~
factorial(4) # The factorial of 4 is 24
factorial(-1)  # Factorial does not exist for negative numbers
~~~
```python
# Solution

def factorial(p_num):
    newFactorial = 1
    if p_num < 0:
        return 'Factorial does not exist for negative numbers'
    for i in range(1, p_num + 1):
        newFactorial *= i
    return f'The factorial of {p_num} is {newFactorial} '

print(factorial(4))
```


## Question 3
Write a program which repeatedly reads numbers until the user enters "done". Once “done” is entered, print out the total, count, and average of the numbers.

If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

Step 1 - Create a function which checks for numbers using try and except block.

Step 2 - Inside while loop ask for input

Step 3 - Calculate count, sum and average
~~~
Enter a number: 2
Enter a number: 4
Enter a number: six
Error, please enter numeric input
Enter a number: 6
Enter a number: done
12.0 3 4.0
~~~
```python
# Solution

def get_number():
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            return 'done'
        try:
            return float(user_input)
        except ValueError:
            print("Error, please enter numeric input")

total = 0
count = 0
average = 0

while True:
    num = get_number()
    if num == 'done':
        break
    total += num
    count += 1

if count > 0:
    average = total / count

print(total, count, average)
```



## Quesrion 4
Write another program that prompts for a list of numbers as we did in previous exercises and at the end prints out both the maximum and minimum of the inputted numbers.

### Input:
~~~
Enter a number: 1
Enter a number: 3
Enter a number: 2
Enter a number: 4
Enter a number: done
~~~

### Output:
~~~
Maximum number: 4.0, Minimum number: 1.0
~~~
```python
# Solution

def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return None




def check():
    numbers = []  

    while True:
        val = input("Enter a number: ")
        if val == 'done':
            break

        float_val = check_for_float(val)
        if float_val is not None:
            numbers.append(float_val)  # Add valid numbers to the list

    if numbers:  
        max_value = max(numbers)
        min_value = min(numbers)
        print(f"Maximum Value: {max_value}, Minimum Value: {min_value}")

    else:
        print("No valid numbers entered")


check()

# Alternatively:
# Solution 2

def check():
    max_value = None
    min_value = None

    while True:
        val = input("Enter a number: ")
        if val == 'done':
            break

        float_val = check_for_float(val)
        if float_val is not None:
            
            
            if max_value is None or float_val > max_value:
                max_value = float_val
            if min_value is None or float_val < min_value:
                min_value = float_val

    if max_value is not None and min_value is not None:
        print(f"Maximum Value: {max_value}")
        print(f"Minimum Value: {min_value}")


check()
```


## Question 5
write a program that randomly generates a number between 1 and 6. When the program runs, it will randomly choose a number between 1 and 6. Then program will print what that number 
is. It should then ask you if you’d like to roll again. 

### Input/Output:
~~~
Dice1: 3 
Dice2: 6
Roll the dice again? (Y/N)
~~~

```python
# Solution

def dice():
    import random
   
    while True:

        diceInput = input('Roll the dice again? (Y/N) ')
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if diceInput.lower() == 'y':
            print(f'Dice1: {dice1}')
            print(f'Dice2: {dice2}')
            continue

        elif diceInput.lower() == 'n':
            break

        else:
            print('Invalid input')


dice()
```


## Question 7
Fizz buzz is a group word game for children to teach them about division. Players take turns to count incrementally, replacing any number divisible by five with the word "Fizz", and any number divisible by seven with the word "Buzz". Write a program where for multiples of 5 you print “Fizz”, for the multiples of 7 “Buzz” and FizzBuzz for multiples of both.
Remember your answer should start from 1 and go up to and including 100.


> `Your program should print each number from 1 to 100 in turn.` 

>   `When the number is divisible by 5 then instead of printing the number it should print "Fizz".` 

>    `When the number is divisible by 7, then instead of printing the number it should print "Buzz".` 

> `And if the number is divisible by both 5 and 7 e.g. 35 then instead of the number it should print "FizzBuzz"`

### Input/Output:

```
1
2
3
4
Fizz
6
Buzz
8
9
Fizz
11
12
13
Buzz
Fizz
```


## Question 6
Create a program that will generate a random number unknown to the user between upper and lower bond that user 
provided. The user needs to guess what that number is. If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. 


* > `Your program should ask for upper and lower bound from the user initially.` 

* >   `Calculate chances of user based on upper and lower bounds.` 

* >    `Based on calculated number of chances ask input from user for guessing the number.` 

* > `If the guessed number is greater than the generated number then print - "You guessed too high", otherwise print 
  "You guessed too low". And finally if the numbers match print - "Congratulations you did it in"`

### Input/Output:

```
Enter Lower bound: 1
Enter Upper bound: 7

    You've only  3  chances to guess the integer!

Guess a number: 4
You Guessed too high!
Guess a number: 1
You guessed too small!
Guess a number: 2
Congratulations you did it in  3  try

The number is 2
    Better Luck Next time!

```
### Hint:
- Log function from math module to calculate chances. (math.log(upper - lower + 1, 2))

```python
# Solution

import math


def GuessingNumber():
    upperBound = int(input("Enter upper bound: "))
    lowerBound = int(input("Enter lower bound: "))

    userChances = math.ceil(math.log(upperBound - lowerBound + 1, 2))

    print(f"\t\t You've only  3  chances to guess the integer!")

    count = 0
    while True:
        guess1 = int(input("Guess a number: "))
        if guess1:
            count += 1

        if guess1 > userChances:
            print("You guessed too high!")

        elif guess1 < userChances:
            print("You guessed too low!")
        elif guess1 == userChances:
            print(f"\t\t Congratulations you did it in  {count} try")
            break

        if count == 3:
            print(f"The number is, {userChances}. ")
            print("\t\t Better Luck Next time!")
            break


GuessingNumber()

```


## Question 7
Fizz buzz is a group word game for children to teach them about division. Players take turns to count incrementally, replacing any number divisible by five with the word "Fizz", and any number divisible by seven with the word "Buzz". Write a program where for multiples of 5 you print “Fizz”, for the multiples of 7 “Buzz” and FizzBuzz for multiples of both.
Remember your answer should start from 1 and go up to and including 100.


> `Your program should print each number from 1 to 100 in turn.` 

>   `When the number is divisible by 5 then instead of printing the number it should print "Fizz".` 

>    `When the number is divisible by 7, then instead of printing the number it should print "Buzz".` 

> `And if the number is divisible by both 5 and 7 e.g. 35 then instead of the number it should print "FizzBuzz"`

### Input/Output:
```
1
2
3
4
Fizz
6
Buzz
8
9
Fizz
11
12
13
Buzz
Fizz
```
```python
# Solution

def fizzBuzz():
    for item in range(1, 100 + 1):
        if item % 5 == 0 and item % 7 == 0:
            print('FizzBuzz')
        elif item % 5 == 0:
            print('Fizz')
        elif item % 7 == 0:
            print('Buzz')

        else:
            print(item)

fizzBuzz()
```


## Question 8
Create a program will generate a password based on user inputs. Initial variables are already provided.
```
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"
```

> `Your program should ask for number of letters, symbols and numbers initially` 

>   `Then based on these inputed values it will generate password` 


### Inpu/Output:

```
How many letters do you want in your password? 8
How many numbers do you want in your password? 2
How many symbols do you want in your password? 2
Your password is: EDUpEYIG67*@

```

# Hint

- Use choice() function from random module to select random character from letters, nums or symbols.

```python
# Solution

import random

def passwordGenerator():

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"
    symbols = "-+=!@#$%^&*"

    userLetter = int(input("How many letters do you want in your password? "))
    userNum = int(input("How many numbers do you want in your password? "))
    userSymbol = int(input("How many symbols do you want in your password? "))

    password = ""
    for i in range(userLetter):
        password += random.choice(letters)
    for i in range(userNum):
        password += random.choice(nums)
    for i in range(userSymbol):
        password += random.choice(symbols)

    print(f'Your password is: {password} ')

    
passwordGenerator()

```



## Question 8
Create a program which simulates Rock, Paper, Scissors Game
Steps:

> `Ask user to select rock, paper or scissors` 

>   `Then generate computer selection by using random module` 

>   `Then determine winner based on computer selection and user selection` 

>   `Finally, ask whether they want to play again or not ` 


Sample Output:

```
Enter a choice (rock, paper, scissors): paper

You chose paper, computer chose scissors.

Scissors cuts paper! You lose.
Play again (Y/N)? Y
Enter a choice (rock, paper, scissors): paper

You chose paper, computer chose scissors.

Scissors cuts paper! You lose.
Play again (Y/N)? Y
Enter a choice (rock, paper, scissors): rock

You chose rock, computer chose paper.

Paper covers rock! You lose.
Play again (Y/N)? 

```

# Hint

- Use choice() function from random module to select random elements from option list.

```python
# Solution

import random

def game():
  
    randomSelect = ["Rock", "Paper", "Scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    userChoice = input("Enter a choice (Rock, Paper, Scissors): ").lower()  

    computerChoice = random.choice(randomSelect)
    print(f"You chose {userChoice}, computer chose {computerChoice}")

    results = {
        ("rock", "scissors"): "Rock crushes scissors! You win.",
        ("scissors", "paper"): "Scissors cuts paper! You win.",
        ("paper", "rock"): "Paper covers rock! You win.",
        ("rock", "paper"): "Paper covers rock! You lose.",
        ("scissors", "rock"): "Rock crushes scissors! You lose.",
        ("paper", "scissors"): "Scissors cuts paper! You lose.",
    }

    if userChoice == computerChoice.lower():  
        print("It's a tie!")
    elif (userChoice, computerChoice.lower()) in results:
        print(results[(userChoice, computerChoice.lower())])
    else:
        print("Invalid input. Please enter Rock, Paper, or Scissors.")

game()
```


## Question 9
Write a python program to get to numbers from the user and output the largest number.

```python
# Solution
def maxNum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = max(num1, num2)
    print(f'The maximum number is: {result}')

maxNum()
```
## Question 10
Fill in the blanks to complete the “all_numbers” function. This function should return a space-separated string of all numbers, from the starting   “minimum” variable  up to and including the “maximum” variable that's passed into the function. Complete the for loop so that a function call like “all_numbers(3,6)” will return the numbers “3 4 5 6”.  

```python

def all_numbers(minimum, maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # numbers up to and including the "maximum" value.
    for ___ 

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        ___ 

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2,6))  # Should be 2 3 4 5 6
print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1,1)) # Should be -1 0 1
print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
print(all_numbers(0,0))  # Should be 0

```

```python
# Solution

def all_numbers(minimum, maximum):
    return_string = ""  # Initializes variable as a string

    for i in range(minimum, maximum + 1):  # Include 'maximum' in the range
        return_string += str(i) + " "  # Convert i to a string before concatenation

    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()

# Test cases
print(all_numbers(2, 6))   # Should be 2 3 4 5 6
print(all_numbers(3, 10))  # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # Should be -1 0 1
print(all_numbers(0, 5))   # Should be 0 1 2 3 4 5
print(all_numbers(0, 0))   # Should be 0

```



