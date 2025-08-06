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


## Question 5
write a program that randomly generates a number between 1 and 6. When the program runs, it will randomly choose a number between 1 and 6. Then program will print what that number 
is. It should then ask you if you’d like to roll again. 

### Input/Output:
~~~
Dice1: 3 
Dice2: 6
Roll the dice again? (Y/N)
~~~


## Question 6
Create a program will generate a random number unknown to the user between upper and lower bond that user provided. The user needs to guess what that number is. If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. 


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

## Question 9
Write a python program to get to numbers from the user and outpt the largest number. 


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

