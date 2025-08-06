## Question 1
Implement a function which takes a string as a parameter and returns new string which is made of the first 2 and the last 2 chars from a given a string. If the length of given string is less than 2 then return empty string.

Example

first_last_characters('appmillers')

### Output
```aprs```

```python
# Solution 1

def first_last_characters(word):
    length = len(word)
    if length < 2:
        return None
    else:
        return  word[0:2] + word[-2:]


word = ("appmillers")
get = first_last_characters(word)
print(get)
```

## Question 2
Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:

Sample output
Please type in a number: 2
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4

```python 
# Solution 1
number  =  int(input("Please Enter A Number: "))
for x in range(1, number + 1 ):
    for y in range(1, number + 1):
        print(f"{x} x {y} = {x * y} ")

# Solution 2 
number  =  int(input("Please Enter A Number: "))
count1 = 1
count2 = 1

while count1 and count2 <= number:
    print(f"{count1} x {count2} = {count1 * count2}")
    count2 +=1
count2 +=1

```

Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

An example of expected behaviour:

Sample output
Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w

```python
# Solution
word = input("Please enter the sentence: ")
newWord = word.split(" ")
for i in newWord:
    print(i[0])

```

## Question 4 
Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.

The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of all positive integers less than or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

Some examples of expected behaviour:

Sample output
Please type in a number: 3
The factorial of the number 3 is 6
Please type in a number: 4
The factorial of the number 4 is 24
Please type in a number: -1
Thanks and bye!

```python

# Solution
import math

while True:
    number = int(input("Pleas enter the number: "))

    if number <=0:
        break
    else:
        print(f"The factorial of the number {number} is {math.factorial(number)}")
print("Thanks and bye!")

```

## Question 5
Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

Sample output
Please type in a number: 5
2
1
4
3
5

```python
# Solution 1


number = int(input("Please enter a number: "))
flip = list(range(1, number + 1))
len_flip = range(0,len(flip), 2)
for i in len_flip:
    if i + 1 < len(flip):
        flip[i], flip[i +1] = flip[i +1],  flip[i]

for num in flip:
    print(num)


# Solution 2
number = int(input("Please type in a number: "))

index = 1
while index + 1 <= number:
    print(index + 1)
    print(index)
    index += 2
#
if index <= number:
    print(index)

```

# Question 6
Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

Sample output
Please type in a number: 5
1
5
2
4
3

```python
# Solution
number = int(input("Please type in a number: "))

# Iterate through the range from 1 to the half of the input number
for i in range(1, (number // 2) + 1):
    # Print the current number and its counterpart from the other end of the range
    print(i)
    print(number - i + 1)

# If the input number is odd, print the middle number
if number % 2 == 1:
    print((number // 2) + 1)

```

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

```python
def patterns(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end=" ")
        print()
    for i in range(n, 0, - 1):
        for j in range(0, i - 1):
            print("*", end=" ")
        print()
new = patterns(5)
print(new)

```

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

```python
def chessboard(size):
    for i in range(size):
        row = ""
        for j in range(size):
            if j % 2 == 0:
                row += "1"
            else:
                row += "0"
        print(row)

chessboard(5)

# Solution 2
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1
```

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

```python
# Solution
def squared(text, length):
    """
    Takes text and length as argument and prints a square of characters.
    
    Args:
    text (str): The input string.
    length (int): The size of the square.
    """
    string = (text * (length ** 2 // len(text) + 1))
    new_string = (string[:length ** 2])
    for index in range(0, length ** 2, length):
        print(new_string[index:index + length])

if __name__ == "__main__":
    squared("abc", 5)

# Solution 2
def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)

```

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
## Solution 
```python 
def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for letter in input_string:
        if letter != " ":
            new_string += letter
            reverse_string = letter + reverse_string

    if new_string.lower() == reverse_string.lower():
        return True

    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

```