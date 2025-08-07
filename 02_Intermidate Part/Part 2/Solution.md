# Question 1
Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

## Output
original [1, 2, 3, 4, 5]

new [2, 4]

# Solution 
```Python
def even_numbers(my_list):
    # Create an empty list to store even numbers
    even_list = []

    # Iterate over each number in the input list
    for num in my_list:
        if num % 2 == 0:  # Check if the number is even
            even_list.append(num)  # Add it to the even_list

    return even_list  # Return the list of even numbers


# Main program
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]  # Input list
    new_list = even_numbers(my_list)  # Call the function
    print("original", my_list)  # Print the original list
    print("new", new_list)  # Print the list of even numbers

```

# Question 2
Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.


## Output 
a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 1]

# Solution 
```python

def  list_sum(a, b):

    sum_of_list = []
    for i in range(len(a)):
        sum_of_list.append(a[i] + b[i])

    return sum_of_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    result = list_sum(a, b)
    print(result)

```

# Question 3
Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]


# Solution 
```python

def distinct_numbers(my_list):
    new_list = sorted(set(my_list))

    return new_list

if __name__ == "__main__":
     
      my_list = [3, 2, 2, 1, 3, 3, 1]
      result = distinct_numbers(my_list)
      print(result)

```

# Question 4
Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)

## Sample output
8
7

# Solution
```python

def length_of_longest(my_list):
    max_length = []
    
    for i in my_list:
        max_length.append(len(i))
    new_list = max(max_length)
    return new_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

```

Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.

my_list = ["first", "second", "fourth", "eleventh"]

result = shortest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = shortest(my_list)
print(result)

## Sample output
first
tim

# Solution 
```python
def shortest(my_list):
    max_length = []
    
    for i in my_list:
        max_length.append((i))
    new_list = min(max_length, key=len)
    return new_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

```

# Question 6
Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.

The order of the strings in the returned list should be the same as in the original.

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result) # ['eleventh']
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

## Output

result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']

# Solution

```python

def all_the_longest(my_list):
    # First loop: determine the maximum length among the words.
    current_max = 0
    for word in my_list:
        if len(word) > current_max:
            current_max = len(word)
    
    # Second loop: collect all the words with length equal to current_max.
    longest = []
    for word in my_list:
        if len(word) == current_max:
            longest.append(word)
    
    return longestfileName = input("Enter file name: ")
fileExt = fileName.split(".")
print(f"the file extension is:", repr(fileExt[-1]))

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)

```

## Question 7
Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

## Solution
```python
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
```

## Question 8
Write a Python program to find out what version of Python you are using.

A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. This string is displayed when the interactive interpreter is started.

## Solution
```python
import sys  # Import the sys module to access system-specific parameters and functions

# Print the Python version to the console
print("Python version")

# Use the sys.version attribute to get the Python version and print it
print(sys.version)

# Print information about the Python version
print("Version info.")

# Use the sys.version_info attribute to get detailed version information and print it
print(sys.version_info)
```

## Question 9
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java

## Solution
```python
# Prompt the user to input a filename and store it in the 'filename' variable
filename = input("Input the Filename: ")

# Split the 'filename' string into a list using the period (.) as a separator and store it in the 'f_extns' variable
f_extns = filename.split(".")

# Print the extension of the file, which is the last element in the 'f_extns' list
print("The extension of the file is : " + repr(f_extns[-1]))

```