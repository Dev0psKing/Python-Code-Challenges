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

## Question 3
Write a virtual coin toss program which will randomly tell the user "Heads" or "Tails".
There are many ways of doing this. But here you should generate a random number, either 0 or 1. Then based on that number we will print out Heads or Tails.
1 means Heads
0 means Tails

#### Expected Output on first play:
~~~
>>Type "play" and press Enter: play
Tails
~~~
#### Expected Output on second play:
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


## Question 10
Define a function which takes a temperature as a parameter and returns the converted temperature.

* return hot if the temperatute is greater than 28
* return warm if the temperature is between 18 and 28
* return cold if the temperature is less than 18.
* return freezing if the temperature is less than 0.

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