# 400+ Python Solved Problems from Beginners to Advanced.


## Question 1
Write a Python program that calculates and displays the union of two sets. Set A and Set B are provided as input, and the program should find the union of these two sets.

### Expected Output:
~~~
Set A: 3, 2, 4, 5, 6, 7, 8
Set B: 4, 12, 5, 1, 6, 8
Union of Set A and Set B: {1, 2, 3, 4, 5, 6, 7, 8, 12}
~~~

```python

#Solution

# Steps/ Algorithm to solve this.
# N.B: Know that you can use pipe methods or union() function to solve this.

# Receive sets as strings and split them into elements
setA = input('Enter your first set (e.g. 3, 2, 4, 5, 6, 7, 8): ')
setB = input('Enter your second set (e.g. 4, 12, 5, 1, 6, 8): ')

# Split the input strings into elements using commas as separators
setA_elements = setA.split(',')
setB_elements = setB.split(',')

# Create sets from the elements
setA = set(map(int, setA_elements))
setB = set(map(int, setB_elements))

setC = setA | setB

print("Union of Set A and Set B:", setC)

# Alternatively
setC = setA.union(setB)

print("Union of Set A and Set B:", setC)

```
Output:
~~~
Set A: {3, 2, 4, 5, 6, 7, 8}
Set B: {4, 12, 5, 1, 6, 8}
Union of Set A and Set B: {1, 2, 3, 4, 5, 6, 7, 8, 12}
~~~

## Question 2

Calculate and print the number of days, weeks, and months in 27 years. Don't worry about leap years!

```Python

# Solution

days = 365 * 27  
weeks = 52 * 27
months = 12 * 27

print('The number of days, weeks, and month for 27 years is:', days, weeks, months)

```
### Output
~~~
The number of days, weeks, and months for 27 years is: 9855 1404 324
~~~

## Question 3

Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.

```Python

# Solution

pi = 3.14159
radius = 5
Area = pi * radius ** 2

print('The area of the circle is: ', Area)

```
### Output
~~~
The area of the circle is: 78.53975
~~~

## Question 4

Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

```Python

# Solution

print(type(10)) #Int

print(type(9.8)) #Float

print(type(('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury'))) #Tuple 

print(type(4 - 4j)) #Complex

print(type(['Uwabor', 'Python', 'Finland'])) #List

print(type({2, 4, 3, 5})) #Set

print(type({'fact': ['Uwabor', 'Python', 'Finland'], 'my_name': 'Collins'})) #Dict

```

### Output
~~~
<class 'int'>
<class 'float'>
<class 'tuple'>
<class 'complex'>
<class 'list'>
<class 'set'>
<class 'dict'>
~~~

## Question 5

Find an Euclidian distance between (2, 3) and (10, 8)

```Python

# Solution

import math

# d = √((x2 - x1)^2 + (y2 - y1)^2)
x2 = 10
x1 = 2
y2 = 8  
y1 = 3

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print('The distance between them is: ', distance)

```
### Output
~~~
The distance between them is:  8.246211251235321
~~~

## Question 6

If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

```Python

# Solution

# Distance in km 
distance_km = 10

# Time in minutes and seconds
time_min = 42  
time_sec = 42

# Convert km to miles
km_to_miles = 0.621371
distance_miles = distance_km * km_to_miles

# Convert time to just seconds 
total_time_sec = (time_min * 60) + time_sec  

# Calculate pace in min/mile
pace_min = int(total_time_sec / distance_miles)
pace_sec = int((total_time_sec / distance_miles) % 60)

print(f"Average Pace: {pace_min} min {pace_sec} sec per mile") 

# Calculate speed in mph
total_time_hrs = total_time_sec / 3600
speed_mph = distance_miles / total_time_hrs

print(f"Average Speed: {speed_mph:.2f} mph")

```
### Output
~~~
Average Pace: 7 min 59 sec per mile
Average Speed: 7.51 mph
~~~

## Question 7

The volume of a sphere with radius r is 4/3 πr^3. What is the volume of a sphere with radius 5?


```Python

# Solution

import math

# Store the radius  
radius = 5

# Calculate volume using formula
volume = (4 / 3) * math.pi * radius ** 3

# Round to 3 decimal places
volume = round(volume, 3)

print(f'The volume of sphere is {volume} ')

```
### Output
~~~
The volume of the sphere is 523.598
~~~

## Question 8

Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

```Python

# Solution

cover_price = 24.95
discount = 0.4  # 40%
shipping_first_book = 3
shipping_additional = 0.75

number_of_books = 60

cost_per_book = cover_price * (1 - discount) 
print(f"Cost per book after discount: {cost_per_book}")

shipping_costs = shipping_first_book + (shipping_additional * (number_of_books - 1))
print(f"Total shipping costs: {shipping_costs}")

total_wholesale_cost = cost_per_book * number_of_books + shipping_costs

print(f"Total wholesale cost for {number_of_books} books is ${total_wholesale_cost}")

```
### Output
~~~
Cost per book after discount: 14.97
Total shipping costs: 47.25
Total wholesale cost for 60 books is $945.45
~~~

## Question 9

Write a program to prompt the user for hours and rate per hours to compute gross pay. you need to take into account 
the result which must be in 2 decimal places.

```Python

## Solution 

hour = float(input('please hour many hours did you work? \n'))

rate = float(input('what was the rate? \n'))

gross_payment = hour * rate

print(round(gross_payment, 2))

```
### Output
~~~
Please enter how many hours did you work? 
10
What was the rate? 
15
150.0
~~~

# Question 10

write a program that converts temperature from Celsius to Fahrenhiet. Using users information.

```Python

# SOlution 

# get input from user
celsius = float(input("Enter temperature in Celsius: "))

# Convert the Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

print(celsius, "degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit")

# N:B == for those not conversant with the formular to solving this I used 
# F = (C * 9/5) + 32

```
### Output
~~~
Enter temperature in Celsius: 25
25.0 degrees Celsius is equal to 77.0 degrees Fahrenheit
~~~
