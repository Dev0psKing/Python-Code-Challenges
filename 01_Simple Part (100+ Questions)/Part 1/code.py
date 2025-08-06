# 400+ Python Solved Problems from Beginner to Advanced


# Question 1

# Write a Python program that calculates and displays the union of two sets. Set A and Set B are provided as input, and the program should find the union of these two sets.

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

# Question 2

# Calculate and print the number of days, weeks, and months in 27 years. Don't worry about leap years!

# Solution
days = 365 * int(input('Enter number of years: '))
weeks = 52 * int(input('Enter number of years: '))
months = 12 * int(input('Enter number of years: '))

print('The number of days, weeks, and month for', input('Enter number of years: '), 'years is:', days, weeks, months)

# Question 3

# Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the
# value of pi.

pi = 3.14159
radius = float(input('Enter the radius: '))
Area = pi * radius ** 2

print('The area of the circle is: ', Area)

# Question 4

# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List,
# Tuple, Set and Dictionary.


# Solution

number = int(input('Enter an integer: '))
print(type(number))  # Int

decimal = float(input('Enter a float: '))
print(type(decimal))  # Float

tuple_input = input('Enter a tuple: ')
tuple_var = tuple(tuple_input.split())
print(type(tuple_var))  # Tuple

complex_num = complex(input('Enter a complex number (a + bj): '))
print(type(complex_num))  # Complex

list_input = input('Enter a list: ')
list_var = list(list_input.split())
print(type(list_var))  # List

set_input = input('Enter a set: ')
set_var = set(set_input.split())
print(type(set_var))  # Set

dict_input = input('Enter a dictionary (key1:value1,key2:value2): ')
dict_var = dict(item.split(":") for item in dict_input.split(","))
print(type(dict_var))  # Dict

# Question 5

# Find an Euclidian distance between (2, 3) and (10, 8)


# Solution

import math

x1 = float(input('Enter x1 value: '))
y1 = float(input('Enter y1 value: '))
x2 = float(input('Enter x2 value: '))
y2 = float(input('Enter y2 value: '))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print('The distance between them is: ', distance)

# Question 6

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?


# Solution

distance_km = float(input('Enter distance in km: '))

time_min = int(input('Enter time in minutes: '))
time_sec = int(input('Enter time in seconds: '))

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

# Question 7

# The volume of a sphere with radius r is 4/3 πr^3. What is the volume of a sphere with radius 5?


# Solution

import math

radius = float(input('Enter radius: '))

# Calculate volume using formula
volume = (4 / 3) * math.pi * radius ** 3

# Round to 3 decimal places
volume = round(volume, 3)

print(volume)

# Question 8

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

cover_price = float(input('Enter cover price: '))
discount = float(input('Enter discount percentage: ')) / 100

shipping_first_book = float(input('Enter shipping cost for first book: '))
shipping_additional = float(input('Enter shipping cost for additional books: '))

number_of_books = int(input('Enter number of books: '))

cost_per_book = cover_price * (1 - discount)
print(f"Cost per book after discount: {cost_per_book}")

shipping_costs = shipping_first_book + (shipping_additional * (number_of_books - 1))
print(f"Total shipping costs: {shipping_costs}")

total_wholesale_cost = cost_per_book * number_of_books + shipping_costs

print(f"Total wholesale cost for {number_of_books} books is ${total_wholesale_cost}")

# Question 9

# Write a program to prompt the user for hours and rate per hours to compute gross pay. you need to take into account
# the result which must be in 2 decimal places.

hour = float(input('please hour many hours did you work? \n'))
rate = float(input('what was the rate? \n'))
gross_payment = hour * rate

print(round(gross_payment, 2))

# Question 10

# write a program that converts temperature from Celsius to Fahrenhiet. Using users information.

celsius = float(input("Enter temperature in Celsius: "))

# Convert the Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

print(celsius, "degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit")
