# 400+ Python Solved Problems from Beginner to Advanced.

## Question 1

Write a program to get a Number from the User, and display the Table for that User.

### Expected Output:
~~~
>> Please enter a number: 2
1		1
2		4
3		9
4		16
5		25
6		36
7		49
8		64
9		81
10		100
~~~

```python
# Solution

number = int(input('Please enter a number: '))
for i in range(1, 11):
    print(f'{i}\t\t{i**number}
```
### Output:
~~~
>> Please enter a number: 2
1		1
2		4
3		9
4		16
5		25
6		36
7		49
8		64
9		81
10		100
~~~

## Question 2

Write a program to get six subject marks from the user and calculate and calculate the total and average marks. 
Display this to the user.

### Expected Output:
~~~
What did you score in math?: 78
What did you score in english?: 83
What did you score in calculus?: 71
What did you score in python?: 98
What did you score in economics?: 87
What did you score in algorithm?: 75
Hello Student! Your totalGrades is: 82.00
~~~

```python
# solution

math = float(input('What did you score in math?: '))
english = float(input('What did you score in english?: '))
calculus = float(input('What did you score in calculus?: '))
python = float(input('What did you score in python?: '))
economics = float(input('What did you score in economics?: '))
algorithm = float(input('What did you score in algorithm?: '))

totalScores = math + english + calculus + python + economics + algorithm
totalSubjects = 6
totalGrades = totalScores / totalSubjects
print(f'Hello Student! Your totalGrades is: {totalGrades :.2f}')

```

## Question 3
Write a virtual coin toss program which will randomly tell the user "Heads" or "Tails".
There are many ways of doing this. But here you should generate a random number, either 0 or 1. Then based on that number we will print out Heads or Tails.
1 means Heads
0 means Tails

#### Expected Output on first play:
~~~
>>Type "play" and press Enter: play
Tail
~~~
#### Expected Output on second play:
~~~
>>Type "play" and press Enter: play
Head
~~~
#### Expected Output invalid input:
~~~
>>Type "play" and press Enter: paly
Invalid input. Please type "play" to flip the coin.
~~~

```python
# Solution

import random

play = input('Type "play" and press Enter: ')

if play == "play":
    result = random.choice(["Heads", "Tails"])
    print(result)
else:
    print('Invalid input. Please type "play" to flip the coin.')
    
 # Alternatively  it can also be solved like this and many other ways.

coin = random.randint(0, 1)
if coin == 1:
    print('Heads')
else:
    print('Tails')

```
#### Output on first play:
~~~
>>Type "play" and press Enter: play
Tails
~~~
#### Output on second play:
~~~
>>Type "play" and press Enter: play
Heads
~~~

#### Expected Output invalid input:
~~~
>>Type "play" and press Enter: paly
Invalid input. Please type "play" to flip the coin.
~~~

## Question 4

Define a function that calculates the area of a square. 

Area of square  = square side x square side

#### input:
~~~
area_of_square(6) 
~~~
#### Output in console:
~~~
36
~~~

```python
# Solution

def area_of_square(side):
    return side * side

print(area_of_square(6))

```

## Question 5

Define a function that converts fluid ounces to milliliters and prints the result to the console. Take into account that 1 fluid ounce is equal to 29.57353 milliliters.

#### input:
~~~
volume_converter(5)) 
~~~
#### Output in console:
~~~
147.86765
~~~

```python
# Solution

def volume_converter(fluid_ounce):
    return fluid_ounce * 29.57353


print(volume_converter(5))
```

## Question 6

We need to paint a wall and we do not know how many cans of paint we need to buy. The instructions on the paint can says that 1 can of paint can cover 4 square meters of wall. So we need to define a function which takes as parameter  height and width of wall and  calculates the area of the wall and based on the area we can calculate number of cans of paint that we need.

Area of wall = wall height  *  wall width

Number of cans of paint that is needed =  Area of wall ÷ coverage per can.
Height = 2, Width = 5, Coverage = 4
Area of wall = 2  *  5  = 10
Number of cans of paint that is needed =  10 ÷ 4 = 2.5
But because you can't buy 2.5 of a can of paint, the result should be rounded up to 3 cans.

#### Input:
~~~
wall_paint(2, 5, 4)
~~~
#### Output:
~~~
3
~~~

```python
# Solution 

import math


def wall_paint(wall_height, wall_width, coverage):
    area_of_wall = wall_height * wall_width
    needed = area_of_wall / coverage
    return needed


wall_height = int(input("Enter height of wall: "))
wall_width = int(input("Enter width of wall: "))

total = wall_paint(wall_height, wall_width, 4)
print(math.ceil(total))
```

## Question 7

Implement a function that takes two strings as parameters and returns their concatenation.

#### Input:
~~~
concatenate("face", "book")
~~~
#### Output:
~~~
facebook
~~~

```python
# Solution

def stringParam(str1, str2):
    return f"{str1}{str2}"

output = stringParam("Face", "book")
print(output)
```


## Question 8
Create a function which takes string password as a parameter and checks the length of password. If the length longer than 8 character it returns True otherwise returns False.

#### Input:
~~~
password_controller("custompassword")
~~~
#### Output:
~~~
True
~~~

```python
# Solution

def password_controllers(str):
    lengthStr = len(str)
    if lengthStr > 8:
        return True
    else:
        return False


output = password_controllers("custompassword")
print(output)
```


## Question 9
Implement code block which asks two numbers and operation (+,-,*,/) that we want to perform on these numbers and returns the result.

#### Input:
~~~
What is the first number? 2
What is the second number? 4
Pick operation from this list (+,-,*,/) *
~~~
#### Output:
~~~
2 * 4 = 8
~~~


```python
# Solution

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return 'Invalid operator'
a = int(input('What is the first number?: '))
b = int(input('What is the second number?: '))
operator = input('Pick operation from this list (+,-,*,/): ')
output =(calculator(a, b, operator))
print(f"{a} {operator} {b} = {output}")
```

## Question 10
Define a function which takes a temperature as a parameter and returns the converted temperature.

* return hot if the temperatute is greater than 28
* return warm if the temperature is between 18 and 28
* return cold if the temperature is less than 18.
* return freezing if the temperature is less than 0.

```python
# Solution

def temperatureChecker(temperature):
    if temperature >= 28:
        return "hot"
    elif temperature >= 18 and temperature < 28:
        return "warm"
    elif temperature < 18:
        return "cold"
    else:
        return "freezing"

temperature = float(input('What is the temperature? '))
output = (temperatureChecker(temperature))
print(output)
```

#### Input:
~~~
28
~~~
#### Output:
~~~
hot
~~~
#### Input:
~~~
18
~~~
#### Output:
~~~
warm
~~~
#### Input:
~~~
0
~~~
#### Output:
~~~
freezing
~~~