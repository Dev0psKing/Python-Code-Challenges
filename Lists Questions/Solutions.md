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

```python
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Indices to remove
remove_indices = {0, 4, 5}

# Use list comprehension to filter
result = [c for i, c in enumerate(colors) if i not in remove_indices]

print(result)
```

