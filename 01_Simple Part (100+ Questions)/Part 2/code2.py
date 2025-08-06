# 400+ Python Solved Problems from Beginner to Advanced

# Question 1

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

# Solution

kilometers = 10
km_to_miles = 1.61

miles = kilometers / km_to_miles

print(miles)

# Question 2 

# How many seconds are there in 42 minutes 42 seconds?

# Solution
minutes = 42
seconds = 42

# Get total seconds in 42 minutes  
minutes_in_seconds = minutes * 60

# Add initial seconds
total_seconds = minutes_in_seconds + seconds

print(total_seconds)

# Question 3

# If I leave my house at 6: 52 am and run 1 mile at an easy pace(8: 15 per mile), 
# then 3 miles at tempo(7: 12 per mile) and 1 mile at easy pace again, 
# what time do I get home for breakfast?

# Solution

import datetime

start_time = datetime.datetime(2023, 2, 15, 6, 52, 0)

print(f"Left home at: {start_time.strftime('%I:%M %p')}")

easy_pace = 8 * 60 + 15  # 8:15 per mile in seconds
tempo_pace = 7 * 60 + 12  # 7:12 per mile in seconds

mile_1 = easy_pace
miles_2_to_4 = tempo_pace * 3
mile_5 = easy_pace

total_time = mile_1 + miles_2_to_4 + mile_5

finish_time = start_time + datetime.timedelta(seconds=total_time)

print(f"Finish time: {finish_time.strftime('%I:%M %p')}")

# Question 4

# Write a program which calculate trip cost for a user.
#   *create a greeting for your program. 
#   *Ask the user for number of days.  
#   *Ask user for hotel price.
#   *Ask the user for rental car price.
#   *Ask for other expenses
#   *combine all expenses and print with 2 digits after decimal 2 places.

# Solution

print('Hello customer! welcome to your cost calculator.')

no_of_days = int(input('How many days will you stay? $'))

hotel_cost = float(input('How much does the hotel cost per night? $'))

flight_cost = float(input('How much does your flight cost? $'))

others = float(input('If you need rental car, please enter the price else press zero, $'))

total = float(no_of_days * hotel_cost + flight_cost + others * no_of_days)

print(f'your total cost is, ${total:.2f}')

# Question 5

# Write a program that takes an integer number from console and checks whether if a number is an odd or even. 

# Solution
number = int(input("What number do you want to check \n"))

if number % 2 == 0:
    print('Yeah! This is an even Number')
else:
    print('Nope! This is an odd number')

# Question 6

#  Write a simple program for a mortgage firm that will enable them to calculate how much interest will be given to their client according to their salaries.
# (1) if the salary is above 2000 then they are qualified for mortgage.If not, they are not qualified for mortgage.
#  (2) if the client has a credit score of 800 and above the interest rate will be 4%.
#  (3)if the credit score is 750 and above the interest rate becomes 6%
#  (4)if the credit score is below 750 the interest rate becomes 8%
#  (5) from their details aske the client if they have disabilities if yes. Give them a discount rate of -2%

# Solution

salary = int(input('What is your monthly salary? $'))
interest_rate = 0

if salary < 2000:
    print('Sorry! You are not eligible for mortgage')

else:
    print('Congratulations you are eligible for mortgage')
    credit_score = int(input('What is your current credit score?: '))
    if credit_score >= 800:
        rate = 4
        print('Your interest rate is 4%')
    elif credit_score >= 750:
        rate = 6
        print('Your interest rate is 6%')
    else:
        rate = 8
        print('Your interest rate is 8%')

    disabilities = input('Hello, Please specify. Do you have any disabilities? Yes or No: ')

    if disabilities == 'Yes':
        rate -= 2
        print(f'Congratulations you have been discounted, your new interest rate is now {rate}% ')



# Question 7

# Write a program that calculates the Body Mass Index (BMI) based on a user's weight and height It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 their weight is normal.
# Over 25 but below 30 they are overweight.
# Over 30 but below 35 they are obese.

# Solution

# formular to solve this is.
# weight in kg / (height in m)^2

weight = float(input('Hello friend! What is your weight please(kg)? '))
height = float(input('Hello friend! What is your height please(m)^2? '))
BMI = round(weight/height ** 2, 2)
if BMI < 18.5:
    print('Hello friend it you are underweight')
elif 18.5 < BMI < 25:
    print('Hello friend your weight is normal')

elif 25 < BMI < 30:
    print('Hello friend you are overweight')
else:
    print('Hello friend you are obese')

# Question 8

# Write a program that calculates final bill Burger Order Price based on a user's choice.
# Price List.
# Mini Burger (M) : $5
# Normal Burger (N): $8
# Large Burger (L) : $10
# Add Mushroom : For Mini and Normal = $1, For Large = $2
# Extra Cheese : $1

# Solution

print("Welcome to burger shop")
size = input('what size of burger do you want? M,N,L ').upper()
mushroom = input('Do you want mushroom Y or N ').upper()
extra_cheese = input('Do you want extra cheese? Y or N ').upper()
bill = 0

if size == 'M':
    bill += 5
elif size == 'N':
    bill += 8
else:
    bill += 10

if mushroom == 'Y':
    if mushroom == "N" or "M":
        bill += 1

    else:
        bill += 2
        print(f'your bill is: {bill}')

if extra_cheese == "Y":
    bill += 1
    print(f'your bill is: {bill}')
else:
    bill += 0
    print(f'your bill is: {bill}')

# Question 9

# Rewrite the Gross Pay Project (Project 3) program to give the employee 1.5 times the hourly rate for hours worked above 40 hours. Here again the program prompts the user for hours and rate per hour to compute gross pay. You need to take into account that the result has exactly two digits after the decimal place.

# Hint: overtime = hour - 40
# Solution

def grossPay(hours, rate):

    if hours < 45:
        return f'Your gross payment is ${bill}'

    elif hours >= 45:
        new_hours_worked = hours - 40
        new_rate_payment = rate * 1.5
        new_gross_payment = new_hours_worked + new_rate_payment
        final_gross_payment = bill + new_gross_payment

        return f'your gross payment is ${final_gross_payment}'

try:
    hours = int(input('Please enter how many hours did you work? '))
    rate = float(input('What was the rate? '))
    bill = hours * rate
    output = (grossPay(hours, rate))
    print(output)

except ValueError :
    print('Input your details correctly')
    quit()
finally:
    print("Thanks for using the program")

hour = float(input('please hour many hours did you work? \n'))
rate = float(input('what was the rate? \n'))
gross_payment = hour * rate

# Alternative Solution

if hour < 45:
    print(round(gross_payment, 2))

elif hour >= 45:
    new_hours_worked = hour - 40
    new_rate_payment = rate * 1.5
    new_gross_payment = new_hours_worked + new_rate_payment
    final_gross_payment = gross_payment + new_gross_payment
    round(final_gross_payment, 2)
    print(f'your gross payment is ${final_gross_payment}')
else:
    print('Input your details correctly')

# Question 10

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
#
# Three criteria must be taken into account to identify leap years:
#
# This is how you work out whether if a particular year is a leap year.
#
# `The year must be evenly divisible by 4;
#  If the year can also be evenly divided by 100, it is not a leap year;
#  unless the year is also evenly divisible by 400`
#
# e.g. The year 2000:

# 2000 ÷ 4 = 500 (Leap)
#
# 2000 ÷ 100 = 20 (Not Leap)
#
# 2000 ÷ 400 = 5 (Leap!)
#
# So the year 2000 is a leap year.

# Solution

print('Hello Welcome to the leap year checker')
year = int(input('What year are you checking?: '))

if year % 4 == 0 or year % 400 == 0:
    print('this is a leap year')

else:
    print('This is not a Leap year')

# Alternative Solution

def leapYear(year):

    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        print('this is a leap year')
    else:
        print('This is not a Leap year')
    return year

year = int(input('What year are you checking?: '))
ouput = leapYear(year)
print(ouput)