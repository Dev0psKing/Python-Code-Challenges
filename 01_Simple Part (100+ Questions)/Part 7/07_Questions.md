## Question 1
Please write a program which asks the user for a year, and prints out the next leap year.

Sample output
Year: 2023
The next leap year after 2023 is 2024

If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

Sample output
Year: 2024
The next leap year after 2024 is 2028

## Question 2
Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

Sample output
Please type in a word: Once
Please type in a word: upon
Please type in a word: a
Please type in a word: time
Please type in a word: there
Please type in a word: was
Please type in a word: a
Please type in a word: girl
Please type in a word: end
Once upon a time there was a girl

Change the program so that the loop ends also if the user types in the same word twice in a row.

Sample output
Please type in a word: It
Please type in a word: was
Please type in a word: a
Please type in a word: dark
Please type in a word: and
Please type in a word: stormy
Please type in a word: night
Please type in a word: night
It was a dark and stormy night

# Question 3
Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

Sample output
Please type in integer numbers. Type in 0 to finish.
Number: 5
Number: 22
Number: 9
Number: -2
Number: 0

Part 1: Count
After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

You will need a new variable here to keep track of the numbers typed in.

Sample output
... the program asks for numbers
Numbers typed in 4

Part 2: Sum
The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

The program should now print out the following:

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34

Part 3: Mean
The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5

Part 4: Positives and negatives
The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5
Positive numbers 3
Negative numbers 1


# Question 4

Please write a program which asks the user to type in an upper limit. The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. That is, the program prints out powers of two in order.

The execution of the program finishes when the next number to be printed would be greater than the limit set by the user. No numbers greater than the limit should be printed.

Sample output
Upper limit: 8
1
2
4
8

# Question 5

Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).

Sample output
Upper limit: 27
Base: 3
1
3
9
2

# Question 6
Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows:

Sample output
Limit: 2
3

Sample output
Limit: 10
10

Sample output
Limit: 18
21

# Question 7

Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:

Sample output
Limit: 2
The consecutive sum: 1 + 2 = 3

Sample output
Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10

Sample output
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21


# Question 8

Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

Some examples of expected behaviour:

Sample output
Please type in string 1: hey
Please type in string 2: hiya
hiya is longer

Sample output
Please type in string 1: howdy doody
Please type in string 2: hola
howdy doody is longer

Sample output
Please type in string 1: hey
Please type in string 2: bye
The strings are equally long

# Question 9

Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a


# Question 10

Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Sample output
Width: 10
Height: 3
##########
##########
##########



