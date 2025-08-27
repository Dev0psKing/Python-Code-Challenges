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

# Solution 

```python

# Write your solution here
# Write your solution here
new_list = []
my_list = []

while True:
    
    user_input = int(input("New item "))

    if user_input == 0:
        print("Bye!")
        break
      

    my_list.append(user_input)
    print(f"The list now: {my_list}")


    new_list.append(user_input)
    sorted_list = sorted(new_list)
    print(f"The list in order: {sorted_list}")

```

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

# SOlution

```Python
def length(param):
    return len(param)

  my_list = [3, 6, -4]
result = length(my_list)
print(result)

```

## Question 3
Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.

my_list = [1, 2, 3, 4, 5]
result = mean(my_list)
print("mean value is", result)

## Sample output
mean value is 3.0

# Solution
```Python

def mean(my_list):
   length = int(len(my_list))
   return sum(my_list) / length

my_list = [3, 6, -4]
result = mean(my_list)
print(result)

```

# Question 4 
Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)

## Sample output
The range of the list is 4

# Solution 
```Python

def range_of_list(my_list):
    min_num = min(my_list)
    max_num = max(my_list)
    total_num = max_num - min_num
    return total_num

my_list = [3, 6, -4]
result = range_of_list(my_list)
print("The range of the list is", result)

```

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

# Solution 
```Python 

user_input = input("Please type in a string: ")

for i in user_input:
    print(i)
    print("*")

```

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

# Solution 

```Python 

user_input = int(input("Please type in a string: "))

for i in range(user_input, 0, -1):
    print(f"-{i}")
for i in range(1, user_input + 1):
    print(f"{i}")

```
# Question 7
Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

Sample output
***
*******
*
*
**

# Solution 

```Python

def list_of_stars(param):
    for i in param:
        print(i * "*")

my_list_of_stars = [3, 7, 1, 1, 2]
result = list_of_stars(my_list_of_stars)
print(result)

```

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

# Solution 

```Python
def anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare sorted versions of the strings
    return sorted(str1) == sorted(str2)
if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java"))

```

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

# Solution 
```Python
def palindromes(word):
    return word == word[::-1]

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

```

# Question 10 
Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)

## Output
The result is 9

# Solution 
```Python


def sum_of_positives(my_list):
    add_list = []
    for i in my_list:
        if i > 0:
            add_list.append(i)  # Append the positive number to add_list
    return sum(add_list)       # Return the sum of positive numbers

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
```