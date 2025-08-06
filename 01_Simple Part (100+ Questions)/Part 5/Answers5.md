# 400+ Python Solved Problems from Beginner to Advanced.

## Question 1
Define a function which takes three integer number as parameters and return the largest number.

### Input Format:
~~~
3
4
2
~~~
### Output Format:
~~~
4
~~~
```python
# Solution

def maxNum(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

output = maxNum(num1, num2, num3)
print(output)
```

# Question 2
A List of scores of students are given, implement a program that calculates the highest score from the given list.
student_scores = [80, 60, 50, 65, 75, 55]
### Input Format:
~~~
student_scores = [80, 60, 50, 65, 75, 55]
~~~
### Output Format:
~~~
The highest score in the class is: 80
~~~

```python
# Solution
def studentScore(student_scores):
    return max(student_scores)

print(f'''The highest score in the class is: {studentScore(student_scores)}')
```

# Question 3
Implement a program which finds integer numbers from given List.

### Input
~~~
custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']
~~~
### Output
~~~
11
30
54
~~~
```python
# Solution
def check(custom_list):
    for i in custom_list:
        new = isinstance(i, int)
        if new == True:
            print(i, "is an integer number")

check(custom_list)
```

# Question 4
Implement a function which takes a List as a parameter and returns the sum of the scores which are above average.
student_scores = [80, 60, 50, 65, 75, 55].

### Input
~~~
student_scores = [80, 60, 50, 65, 75, 55]
~~~
### Output
~~~
220
~~~
Hint : DO NOT use any built in function such as sum() and len()!
```python
# Solution

student_scores = [80, 60, 50, 65, 75, 55]

def averageScores(student_scores):
    
    total = 0
    count = 0
    for score in student_scores:
        total += score
        count += 1
    return total/count

def sum_score_above_average(student_scores):
    
    total = 0
    for score in student_scores:
        if score > averageScores(student_scores):
            total += score
    return total

print(sum_score_above_average(student_scores))
```


# Question 5
Implement a function that calculates the sum of all odd numbers from 1 to 100 by using range() function inside loop.

### Input
~~~
1+3+5+...+97+99 = 2500
~~~
### Output
~~~
2500
~~~
```python
# Solution

def add_odd_numbers():
    sum = 0
    for i in range(1, 100,2):
        sum += i
    return sum

print(add_odd_numbers())
```


# Question 6
Implement a function with two parameters that calculates the sum of all even numbers from 1 to 100 by using range() 
function.

### Input
~~~
1+3+5+...+97+99
~~~
### Output
~~~
2550
~~~

```python
# Solution

def add_even_numbers(start, end):
    sum = 0
    for i in range(start, end+1):
        if i % 2 == 0:
            sum += i
    return sum

print(add_even_numbers(1, 100))
```


# Question 7
Write a Python program that demonstrates input and output for various primitive and derived data types. Use the input() function to perform input, and the print() function to display the output.

### Input
~~~
Enter a character: C

Enter a signed short value: -32768
~~~
### Output:
~~~
You entered character: 'C'

You entered signed short: -32768
~~~

```python
# Solution

# inputs

print('PLEASE ENTER THE FOLLOWING INSTRUCTIONS')
char = input('Enter a character:')
char2 = input('Enter another character:')
shortValue = int(input('Enter a signed short value:'))
unsignedShortValue = int(input('Enter an unsigned short value:'))
inteValue = int(input('Enter an signed integer value:'))
unsignedIntValue = int(input('Enter an unsigned integer value:'))
longValue = int(input('Enter a signed long value:'))
signedLongValue = int(input('Enter an unsigned long value:'))
extraLongValue = int(input('Enter a signed long long value:'))
unsigneExtraLongValue = int(input('Enter an unsigned long long value:'))
floatValue = float(input('Enter a float value:'))
doubleValue = int(input('Enter a double value:'))
longdoubleValue = int(input('Enter a long double value:'))

# Outputs
print(f"You entered character: '{char.upper()}'")
print(f"You entered character: '{char2.upper()}'")
print(f'You entered signed short: {shortValue} ')
print(f'You entered unsigned short: {unsignedShortValue} ')
print(f'You entered signed int: {inteValue} ')
print(f'You entered unsigned int: {unsignedIntValue} ')
print(f'You entered signed long: {signedLongValue} ')
print(f'You entered unsigned long: {unsigneExtraLongValue} ')
print(f'You entered float: {floatValue} ')
print(f'You entered double: {doubleValue}')
print(f'You entered long double: {longdoubleValue} ')
```


# Question 8
Write a Python program to input two numbers from user and calculate their sum. Python program to add two numbers and 
display their sum as output. 

### Input:
~~~
Input first number: 20
Input second number: 10
~~~
### Output:
~~~
The sum of 20 and 80 is 100
~~~

```python
# Solution

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

print(f'The sum of {num1} and {num2} is {num1 + num2}')
```


# Question 9
Write a Python program to input length and width of a rectangle and calculate perimeter of the rectangle. How to find 
perimeter of a rectangle in Python programming.

### Hints:
Perimeter of rectangle is given by the below formula:
Perimeter of rectangle = 2(l + w)
Where l is length and w is the width of rectangle.

### Input:
~~~
Enter length: 5
Enter width: 10
~~~
### Output:
~~~
Perimeter of rectangle = 30 units
~~~

```python
# Solution

import math

length = int(input("Enter length of a rectangle: "))
width = int(input("Enter width of a rectangle: "))

# formular for perimeter of rectangle = 2(l + w)

perimeterOfRectangle = 2 * (length + width)
print(f"Perimeter of rectangle = {perimeterOfRectangle} units")
```


# Question 10
Implement a while loop which gets continuously username from console by using input function and terminates when the input is equal to "test".

### Example
~~~
Enter username: test1
Enter username: test2
Enter username: test3
~~~

```python
# Solution

username = ' '
while username != 'test' and username != 'test1':
    username = input("Enter username: ")

    print(username)
```