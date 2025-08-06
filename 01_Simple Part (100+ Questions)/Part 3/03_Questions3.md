# 400+ Python Solved Problems from Beginner to Advanced.

## Question 1

Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and
1.0, print a grade using the following table:  

| Grade | Score | 
|-------| --- |
| A     | >= 0.9 | 
| B     | >= 0.8 | 
| C     | >= 0.7 | 
| D     | >= 0.6 | 
|  F    | < 0.6 | 

# Expected Ouput:
~~~
Enter score: perfect
> Bad score
Enter score: 10.0
> Bad score
Enter score: 0.75
> C
Enter score: 0.5
> F

~~~
# Question 2

Write a Python function called longest_word that takes three input strings as arguments: word1, word2, and word3. The function should determine and return the longest word among the three input words. Use the logic demonstrated in the following examples:

~~~
print(longest_word("chair", "couch", "table"))   # Output should be: "chair"
print(longest_word("bed", "bath", "beyond"))     # Output should be: "beyond"
print(longest_word("laptop", "notebook", "desktop"))  # Output should be: "notebook"

~~~
Your function should be able to correctly identify the longest word among the input strings and return it as the output.

### Expected Output

~~~
chair
beyond
notebook
~~~

## Question 3

Write a program to test the compatibility between two people.  

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 


For Love Scores **less than 10** or **greater than 85**, the message should be:

`"Your score is **x**, you go together like coke and mentos."` 

For Love Scores **between 40** and **70**, the message should be:

`"Your score is **y**, you are alright together."`

Otherwise, the message will just be their score. e.g.:

`"Your score is **z**."`

Example 

`name1 = "David"`

`name2 = "Jennifer"`

T occurs 0 times

R occurs 1 time

U occurs 0 times

E occurs 2 times

Total = 3

L occurs 0 time

O occurs 0 times

V occurs 1 times

E occurs 2 times

Total = 3

Love Score = 33

Print: "Your score is 33."

 score is 33.

### Expected Output:
~~~
Welcome to Love Calculator
What is your name? David
What is the name of your lover? Jennifer
Your score is 33.
~~~
# Hint

1. The `lower()` function changes all the letters in a string to lower case. 

2. The `count()` function will give you the number of times a letter occurs in a string. 

## Question 4

write a program to show such type of layouts of numbers, squares, and cube.

### Expected Output:
~~~
Number    Square   Cube
1         1        1
2         4        8
3         9        27
4         16       64
5         25       125
~~~

## Question 5

Write a program that displays name and age of users.

### Expected Output
~~~
Hi Sarah Uwabor! Your age is 24.
~~~


## Question 6

Write a program that takes the age as input from the user and checks if the user is eligible to participate in voting. If the age is less than 18, they are not eligible to vote, and the program should provide a reason for their ineligibility.

### Expected Output If the user's age is 20 (eligible to vote):
~~~
Enter your full name: Sarah Uwabor
Enter your age: 20
Congratutions! Sarah Uwabor, You are eligible to vote.
~~~
### Expected Output If the user's age is 16 (not eligible to vote):
~~~
Enter your age: 16
Sorry! Sarah Uwabor, you are not eligible to vote. You have to be 18 and above to vote.
~~~
### Expected Output If the user enters a non-numeric input:
~~~
Enter your age: Sarah
please enter a numeric number for your age.
~~~

## Question 7

Write a program that performs all arithmetic operations (addition, subtraction, multiplication, division) on two variables provided by the user.

### Expected Output Addition:
~~~
Enter the first number: 5
Enter the second number: 3
Sum: 8
~~~
### Expected Output Subtraction:
~~~
Enter the first number: 10
Enter the second number: 4
Difference: 6
~~~
### Expected Output Multiplication:
~~~
Enter the first number: 6
Enter the second number: 7
Product: 42
~~~
### Expected Output Division:
~~~
Enter the first number: 8
Enter the second number: 2
Quotient:= 4
~~~


## Question 8

Write strings on the python interactive shell. The strings are the following:

* Your name
* Your Surname
* Your country
* I am Crushing Python Questions
### Expected Output
~~~
My name is Collins Uwabor from Nigeria and I am Crushing Python Questions.
~~~


## Question 9

Write a Python program that calculates and displays the intersection of two sets. Set A and Set B are provided as 
input, and the program should find the union of these two sets.

### Expected Output:
~~~
Set A: 3, 2, 4, 5, 6, 7, 8
Set B: 4, 12, 5, 1, 6, 8
Intersection of Set A and Set B:{8, 4, 5, 6}
~~~


## Question 10

Write a Python program that calculates the difference of two sets. Set A and Set B are provided as 
input, and the program should find the union of these two sets.

### Expected Output:
~~~
Set A: 3, 2, 4, 5, 6, 7, 8
Set B: 4, 12, 5, 1, 6, 8
difference of Set A and Set B:{2, 3, 7}
~~~



