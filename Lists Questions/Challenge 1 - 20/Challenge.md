### Question 
Write a Python program to sum all the items in a list.

### Solution 
```python
listItem = [1,2,3,4,5,6,7,8,9,0]
sumItem = 0

for i in listItem:
    sumItem += i
print(sumItem)

# Alternative using inbuilt function
sumListItem = sum(listItem)
print(sumListItem)
    
```

### Question
Write a Python program to multiply all the items in a list.
```python 
listItem = [1,2,3,4,5,6,7,8,9]
sumItem = 1

for i in listItem:
    sumItem *= i
print(sumItem)

# Alternative using inbuilt function
import math
sumListItem = math.prod(listItem)
print(sumListItem)
```

### Question 
Write a Python program to get the largest number from a list.

```python
listItem = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# start by assuming the first number is the largest
highest = listItem[0]

for i in listItem:
    if i > highest:
        highest = i

print("Highest number is:", highest)

# Alternatively

listHighest = max(listItem)
print("Highest number is:", listHighest)
```

### Question 
Write a Python program to get the smallest number from a list.
```python
listItem = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# start by assuming the first number is the largest
smallest = listItem[0]

for i in listItem:
    if i < smallest:
        smallest = i

print("smallest number is:", smallest)

# Alternatively

listSmallest = min(listItem)
print("smallest number is:", listSmallest)
```


### Question 
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
```python
listeItem = ['abc', 'xyz', 'aba', '1221']
countList = 0

for i in listeItem:
    if len(i) >= 2 and i[0] == i[-1]:
        countList += 1

print("Count:", countList)
```
### Question 
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

```python
listItem =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sort_list = sorted(listItem, key=lambda x: x[1])

print(sort_list)
```

### Question
Write a Python program to remove duplicates from a list.

```python
listItem =  [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

dup_list = set(listItem)
newList = list(dup_list)

print(newList)
```


### Question
Write a Python program to check if a list is empty or not.
```python
mylist = []

if not mylist:
    print("List is empty")
else:
    print("List is not empty")
```
### Question
Write a Python program to clone or copy a list.
```python 
listItem =  [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

copyList = listItem[:]
print(copyList)

# Alternatively
dup_list = listItem.copy()
print(dup_list)
```

### Question
Write a Python program to access the index of a list.

```python
listItem =  [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

for index, item in enumerate(listItem):
    print(index, item)
```

### Question
Write a Python program to find the list of words that are longer than n from a given list of words.

### Solution
```python
# Define a function called 'long_words' that takes an integer 'n' and a string 'str' as input
def long_words(n, str):
    # Create an empty list 'word_len' to store words longer than 'n' characters
    word_len = []

    # Split the input string 'str' into a list of words using space as the delimiter
    txt = str.split(" ")

    # Iterate through each word 'x' in the list of words 'txt'
    for x in txt:
        # Check if the length of the current word 'x' is greater than 'n'
        if len(x) > n:
            # If the word is longer than 'n' characters, add it to the 'word_len' list
            word_len.append(x)

    # Return the list of words longer than 'n' characters
    return word_len

# Call the 'long_words' function with an 'n' value of 3 and a string as input, and print the result
print(long_words(3, "The quick brown fox jumps over the lazy dog"))
```

### Question
Write a Python function that takes two lists and returns True if they have at least one common member.

### Solution
```python 
def twoLists(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
    return result

print(twoLists([1,2,3,4,5],[6,7,8,7,9]))
```

### Question
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

### Solution
```python
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Indices to remove
remove_indices = {0, 4, 5}

# Use list comprehension to filter
result = [c for i, c in enumerate(colors) if i not in remove_indices]

print(result)
```

### Question
Write a Python program to print the numbers of a specified list after removing even numbers from it.
###  Solution
```python
list = [1,2,4,5,6,7,8,9,12,123,120,40,16,2,3,5,7,8,99,12,13,23]

listEven = []

for i in list:
    if i % 2 != 0:
        listEven.append(i)
print(listEven)
```
### Question
Write a Python program to shuffle and print a specified list.

```python
# Import the 'shuffle' function from the 'random' module, which is used for shuffling the elements in a list
from random import shuffle

# Create a list 'color' with several color strings
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Use the 'shuffle' function to randomly reorder the elements in the 'color' list
shuffle(color)

# Print the shuffled 'color' list, which will have its elements in a random order
print(color)
```

### Question

Write a Python program to generate and print a list of square numbers between 1 and 30 (both included).
From this list, print the first 5 elements and the last 5 elements separately.

Expected Output:
Square numbers between 1 and 30: [1, 4, 9, 16, 25]  
  
### Solution
```python
result = []

for i in range(1, 31):
    listSquares = i * i
    if listSquares >= 30:
        break
    result.append(listSquares)
print(result)
```
### Question 
Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False

### Solution

```python
def is_prime(n):
    if n <= 1:  # 0 and 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

def all_primes(numbers):
    for num in numbers:
        if not is_prime(num):  # if any number is not prime
            return False
    return True

# Test cases
print(all_primes([0, 3, 4, 7, 9]))   # False
print(all_primes([3, 5, 7, 13]))     # True
print(all_primes([1, 5, 3]))         # False
```
### Question
Write a Python program to generate all permutations of a list in Python.

```python
# Import the 'itertools' module, which provides various functions for working with iterators
import itertools

# Use 'itertools.permutations' to generate all permutations of the list [1, 2, 3], and convert the result to a list
# This will produce all possible orderings of the elements in the list
print(list(itertools.permutations([1, 2, 3])))

Sample Output:

[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] 
```

### question
Write a Python program to calculate the difference between the two lists.

### Solution
```python 
# Define a list 'list1' containing numbers
list1 = [1, 3, 5, 7, 9]

# Define another list 'list2' containing different numbers
list2 = [1, 2, 4, 6, 7, 8]

# Calculate the difference between 'list1' and 'list2' by converting them to sets and subtracting the sets
diff_list1_list2 = list(set(list1) - set(list2))

# Calculate the difference between 'list2' and 'list1' by converting them to sets and subtracting the sets
diff_list2_list1 = list(set(list2) - set(list1))

# Concatenate the differences 'diff_list1_list2' and 'diff_list2_list1' to obtain a list of all unique differences
total_diff = diff_list1_list2 + diff_list2_list1

# Print the total difference, which represents elements that are unique to each list
print(total_diff)

Sample Output:
[9, 3, 5, 8, 2, 4, 6]
```
