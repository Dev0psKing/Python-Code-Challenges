Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

Sample output
Please type in a string: Hi there!

Hi there!
---------
Please type in a string: This is a test

This is a test
--------------
Please type in a string: a

a
-
Please type in a string

```python

while True:
    word = input("Please type in a string: ")

    if word == "":
        break

    print(word)
    print('-' * len(word))
    print()

```

# Question 2

Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Sample output
Please type in a string: python

**************python
Sample output
Please type in a string: alongerstring

*******alongerstring
Sample output
Please type in a string: averyverylongstring

*averyverylongstring

```python

word = input("Please type in a string: ")

num = 20 - len(word)
star = "*"
new_word =  star * num
print(new_word + word)

```

# Question 3

Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Sample output
Word: testing

******************************
*          testing           *
******************************
Sample output
Word: python

******************************
*           python           *
******************************

# Solution
```python
word = input("Word: ")
 
print("*" * 30)
spaces_at_start = (28 - len(word)) // 2
spaces_at_end = spaces_at_start
 
# If the word length is odd, one is added to the spaces at the end of the word
# to get all 30 characters filled
if len(word) % 2 != 0:
    spaces_at_end += 1
 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30)

```

# Question 4 

Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
te
tes
test

# Solution

```python

## Solution 1

word = input("Please enter the word:")

for letter in range(1, len(word) + 1):
    print(word[0:letter])

## Solution 2

string = 1
while string <= len(word):
    print(word[:string])
    string +=1

## Solution 3

substring = ""
for letter in word:
    substring += letter
    print(substring)

```

# Question 5

Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
st
est
test

```python
# Solution 1

start = len(user_input) -1
while start >= 0:
    print(user_input[start:])
    start -= 1

# Solution 2

user_input = input("Please type in a string: ")

# Reverse the input string
reversed_input = user_input[::-1]

# Iterate through all possible substrings of the reversed input string
for i in range(len(reversed_input)):
    substring = reversed_input[:i+1]
    print(substring[::-1])

```

# Question 6

Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

Sample output
Please type in a string: hello there
a not found
e found
o found

Sample output
Please type in a string: hiya
a found
e not found
o not found

```python
# Solution 1

word = input("Enter the word: ")

vowels = "aeo"

for vowel in vowels:
    if vowel in word:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")

# Solution 2

# Write your solution here

# Please type in a string: hello there
# a not found
# e found
# o found
#
# Sample output
# Please type in a string: hiya
# a found
# e not found
# o not found

word = input("Enter the word: ")

a = "a"
e = "e"
o = "o"

if a in word:
    print("a found")
else:
    print("a not found")

if e in word:
    print("e found")
else:
    print("e not found")

if o in word:
    print("o found")
else:
    print("o not found")

```

# Question 7
Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.

Sample output
Please type in a word: mammoth
Please type in a character: m
mam

Sample output
Please type in a word: banana
Please type in a character: n
nan

Sample output
Please type in a word: tomato
Please type in a character: x
Sample output
Please type in a word: python
Please type in a character: n

```python
# Solution 1

word = input("Please type in a string: ")
character = input("Please type in a single character: ")

index = word.find(character)

if index != -1 and index < len(word) - 2:
    print(word[index:index+3])

# Solution 2

word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = word.find(character)
if index!=-1 and len(word)>=index+3:
    print(word[index:index+3])
 
```

# Question 8
Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

Sample output
Please type in a word: mammoth
Please type in a character: m
mam
mmo
mot

Sample output
Please type in a word: banana
Please type in a character: n
nan

```python 
# Solution

word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)

while index != -1:
    if index <= len(word) - 3:
        print(word[index:index + 3])
    index = word.find(character, index + 1)

   ```
# Question 9

Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:

Sample output
Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output
Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output
Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string.


```python
text = input("Please type in a string: ")
sub = input("Please type in a substring: ")

first_index = text.find(sub)
if first_index == -1:
  print("The substring does not occur twice in the string.")
else:
  second_index = text.find(sub, first_index + len(sub))
  
  # Check if there's a second occurrence and print accordingly
  if second_index == -1:
    print("The substring does not occur twice in the string.")
  else:
    print(f"The second occurrence of the substring is at index {second_index}.")  
```

# Question 10
Create a function that takes two digit number from console and returns sum of digits. e.g. if the input was 45, then the output should be 4 + 5 = 9

Example Input

sum_of_two_digits()
Enter two digit number: 45 
Output

4 + 5  = 9

```python

# Solution 1
def sum_of_numbers():
    number = input("Please enter at least 2 numbers: ")
    list_num = list(number)
    add_num = [int(num) for num in list_num if num.isdigit()]
    total = sum(add_num)
    print(total)
    return total
sum_of_numbers()

# Solution 2
def sum_of_numbers():
    number = input("Please enter at least 2 numbers: ")
    add_num = int(number[0]) + int(number[1])
    print(add_num)
    return add_num
sum_of_numbers()

```