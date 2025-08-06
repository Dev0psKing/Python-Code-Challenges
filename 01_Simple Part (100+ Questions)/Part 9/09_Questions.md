## Question 1
Implement a function which takes a string as a parameter and returns new string which is made of the first 2 and the last 2 chars from a given a string. If the length of given string is less than 2 then return empty string.

Example

first_last_characters('appmillers')

### Output
```aprs```

## Question 2
Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:

### Sample output
Please type in a number: 2
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4

## Question 3
Please write a program which asks the user to type in a sentence. The program then prints out the first letter of 
each word in the sentence, each letter on a separate line.

An example of expected behaviour:

Sample output
Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w

## Question 4 
Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.

The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of all positive integers less than or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

Some examples of expected behaviour:

### Sample output
Please type in a number: 3
The factorial of the number 3 is 6
Please type in a number: 4
The factorial of the number 4 is 24
Please type in a number: -1
Thanks and bye!

## Question 5
Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

### Sample output
Please type in a number: 5
2
1
4
3
5

# Question 6
Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

### Sample output
Please type in a number: 5
1
5
2
4
3

# Question 7
Create a function which takes as parameter integer number (n) and based on this number it prints the following start pattern using nested loop and string formatting. So if n equals 5 the maximum number of stars (*) will be 5 in the pattern.

Example1

print_pattern(5)

### Output1

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

# Question 8 
Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:
### Sample output
101
010
101

101010
010101
101010
010101
101010
010101

#  Question 9
Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

## Sample output
aba
bab
aba

aybab
tuayb
abtua
ybabt
uayba

# Question 10
Write a Python function named is_palindrome `(input_string)` that determines whether a given string is a palindrome, 
ignoring spaces and case sensitivity. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
Your function should return True if the input string is a palindrome and False otherwise.

## Output
```python
print(is_palindrome("Never Odd or Even")) # Should return True
print(is_palindrome("abc")) # Should return False
print(is_palindrome("kayak")) # Should return True
```

