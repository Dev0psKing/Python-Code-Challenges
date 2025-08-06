# Question 1

Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:

in the order the items were added
ordered from smallest to greatest
The program exits when the user types in 0.

## Sample output

New item: 3
The list now: [3]
The list in order: [3]
New item: 1
The list now: [3, 1]
The list in order: [1, 3]
New item: 9
The list now: [3, 1, 9]
The list in order: [1, 3, 9]
New item: 5
The list now: [3, 1, 9, 5]
The list in order: [1, 3, 5, 9]
New item: 0
Bye!

# Question 2
Please write a function named length which takes a list as its argument and returns the length of the list.

my_list = [1, 2, 3, 4, 5]
result = length(my_list)
print("The length is", result)

## Output 
result = length([1, 1, 1, 1])
print("The length is", result)
Sample output
The length is 5
The length is 4

## Question 3
Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.

my_list = [1, 2, 3, 4, 5]
result = mean(my_list)
print("mean value is", result)

## Sample output
mean value is 3.0

# Question 4 
Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)

## Sample output
The range of the list is 4


# Question 5 
Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.

This is how it should work:

## Sample output
Please type in a string: Python
P
*
y
*
t
*
h
*
o
*
n
*

# Question 6
Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line.

An example of expected behaviour:

## Sample output
Please type in a positive integer: 4
-4
-3
-2
-1
1
2
3
4

# Question 8
Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

## Outputs
print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False

Hint: the function sorted can be used on strings as well.

# Question 9
Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.

Please also write a main program which asks the user to type in words until they type in a palindrome:

## Output
Please type in a palindrome: python
that wasn't a palindrome
Please type in a palindrome: java
that wasn't a palindrome
Please type in a palindrome: oddoreven
that wasn't a palindrome
Please type in a palindrome: neveroddoreven
neveroddoreven is a palindrome!

# Question 10 
Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)

## Output
The result is 9