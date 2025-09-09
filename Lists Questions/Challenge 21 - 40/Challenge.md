### Question 
Write a Python program to append a list to the second list.

```python 
# Define a list 'list1' containing numeric elements
list1 = [1, 2, 3, 0]

# Define another list 'list2' containing string elements
list2 = ['Red', 'Green', 'Black']

# Concatenate 'list1' and 'list2' to create a single list 'final_list'
final_list = list1 + list2

# Print the 'final_list,' which contains elements from both 'list1' and 'list2'
print(final_list)

Sample Output:
[1, 2, 3, 0, 'Red', 'Green', 'Black']

```

### Question
Write a Python program to select an item randomly from a list.

### Solution
```python
# Import the 'choice' function from the 'random' module to select a random element from a list

from random import choice

# Define a function named 'random_element' that takes a list 'lst' as a parameter
def random_element(lst):
    # Use the 'choice' function to return a random element from the input list 'lst'
    return choice(lst)

# Call the 'random_element' function with a list as an argument and print the randomly selected element
print(random_element([2, 3, 4, 7, 9, 11, 15]))
```

### Question
Write a Python program to find the second largest number in a list.

### Solution
```python
# Define a function named 'second_largest' that takes a list of numbers 'numbers' as a parameter
def second_largest(numbers):
    # Check if the length of the 'numbers' list is less than 2; return None in this case
    if len(numbers) < 2:
        return

    # Check if there are only two elements in the 'numbers' list, and they are the same; return None in this case
    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return

    # Create an empty set 'dup_items' to store duplicate items and an empty list 'uniq_items' to store unique items
    dup_items = set()
    uniq_items = []

    # Iterate through the elements in the 'numbers' list
    for x in numbers:
        # Check if 'x' is not in 'dup_items'; if not, add it to 'uniq_items' and 'dup_items'
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    # Sort the 'uniq_items' list in descending order (largest first)
    uniq_items.sort(reverse=True)

    # Return the second largest item from the sorted 'uniq_items' list, which is at index 1
    return uniq_items[1]

# Call the 'second_largest' function with different lists and print the results
print(second_largest([1, 2, -8, -2, 0, -2]))   # → 1
print(second_largest([1, 1, 0, 0, 2, -2, -2])) # → 1
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2])) # → 1
print(second_largest([2, 2]))  # → None
print(second_largest([2]))     # → None


# Alternative 
lst = [1, 2, 3, 4, 5, 6, -7, 8, 9, -10]

# Remove duplicates just in case
unique_lst = list(set(lst))
unique_lst.sort()

second_largest = unique_lst[-2]
print("Second Largest:", second_largest)
```

### Question
Write a Python program to get the frequency of elements in a list.

### Solution 
```python
# Import the 'collections' module, which provides specialized container data types
from collections import Counter

# Define a list 'my_list' containing multiple numbers, including duplicates
my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

# Print the original list 'my_list'
print("Original List : ", my_list)

# Use the 'collections.Counter' function to count the frequency of each element in 'my_list' and store it in 'ctr'
lstFreq = Counter(my_list)

# Print the frequency of the elements in the list, as provided by the 'ctr' object
print("Frequency of the elements in the List : ", lstFreq) 

```

### Question 
Write a Python program to count the number of elements in a list within a specified range.

### Solution 
# Define a function named 'count_range_in_list' that counts the number of elements within a specified range
def count_range_in_list(li, min, max):
    # Initialize a counter 'ctr' to keep track of the count
    ctr = 0

    # Iterate through the elements 'x' in the input list 'li'
    for x in li:
        # Check if 'x' falls within the specified range [min, max]
        if min <= x <= max:
            # If 'x' is within the range, increment the counter 'ctr'
            ctr += 1

    # Return the final count of elements that fall within the range
    return ctr

# Define a list 'list1' containing numeric elements
list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]

# Call the 'count_range_in_list' function with 'list1' and the range [40, 100], and print the result
print(count_range_in_list(list1, 40, 100))

# Define another list 'list2' containing character elements
list2 = ['a', 'b', 'c', 'd', 'e', 'f']

# Call the 'count_range_in_list' function with 'list2' and the range ['a', 'e'], and print the result
print(count_range_in_list(list2, 'a', 'e')) 

### Question
Write a Python program to check whether a list contains a sublist.

### Solution
```python
# Define a function named 'is_Sublist' that checks if list 's' is a sublist of list 'l'
def is_Sublist(l, s):
    sub_set = False  # Initialize a flag 'sub_set' to indicate whether 's' is a sublist of 'l

    # Check if 's' is an empty list; in this case, 's' is a sublist of any list
    if s == []:
        sub_set = True
    # Check if 's' is equal to 'l'; if so, 's' is a sublist of 'l
    elif s == l:
        sub_set = True
    # Check if the length of 's' is greater than the length of 'l'; 's' cannot be a sublist in this case
    elif len(s) > len(l):
        sub_set = False
    else:
        # Iterate through the elements of 'l'
        for i in range(len(l)):
            # Check if the current element in 'l' matches the first element in 's'
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                # If 'n' equals the length of 's', 's' is a sublist of 'l
                if n == len(s):
                    sub_set = True

    # Return the value of 'sub_set,' which indicates whether 's' is a sublist of 'l

    return sub_set

# Define list 'a,' 'b,' and 'c'
a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]

# Check if 'b' is a sublist of 'a' and print the result
print(is_Sublist(a, b))

# Check if 'c' is a sublist of 'a' and print the result
print(is_Sublist(a, c)) 

# Alternatively 
def contains_sublist(main_list, sublist):
    """Check if main_list contains sublist"""
    if not sublist:
        return True
    n, m = len(main_list), len(sublist)
    return any(main_list[i:i + m] == sublist for i in range(n - m + 1))

# Example usage
main = [1, 2, 3, 4, 5]
sub = [1, 2, 3]
sub2 = [1, 2, 5]
print(contains_sublist(main, sub))  # Output: True
print(contains_sublist(main, sub2)) # Output False
```

### Question 
Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.

Note: In mathematics, the sieve of Eratosthenes (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous), one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.

### Solution
```python
# Define a function named 'prime_eratosthenes' that generates prime numbers using the Sieve of Eratosthenes algorithm
def prime_eratosthenes(n):
    prime_list = []  # Create an empty list to store prime numbers
    # Iterate through the numbers from 2 to 'n'
    for i in range(2, n+1):
        if i not in prime_list:
            # If 'i' is not in the 'prime_list,' it's a prime number; print it
            print(i)

            # Mark all multiples of 'i' as non-prime by adding them to 'prime_list'
            for j in range(i*i, n+1, i):
                prime_list.append(j)

# Call the 'prime_eratosthenes' function with 'n' set to 100 to generate prime numbers
# The function does not have a return value, so it prints the prime numbers directly
prime_eratosthenes(100)
```

### Question 
Write a Python program to create a list by concatenating a given list with a range from 1 to n.

### Solution
```python
def concatenate_list(base_list, n):
    result = []
    for i in range(1, n+1):
        for item in base_list:
            result.append(f"{item}{i}")
    return result

# Example usage
sample_list = ['p', 'q']
n = 5
output = concatenate_list(sample_list, n)
print(output)

# Alternative way

# Define a list 'my_list' containing elements 'p' and 'q'
my_list = ['p', 'q']

# Define a variable 'n' with the value 4
n = 4

# Use a list comprehension to create a new list 'new_list' by combining elements from 'my_list' with numbers from 1 to 'n'
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]

# Print the 'new_list' containing combinations of elements from 'my_list' and numbers
print(new_list)
```
## Question
Write a Python program to split a list every Nth element.

## Solution
```python
# Define a list 'C' containing alphabetic characters from 'a' to 'n'
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# Define a function 'list_slice' that takes a sequence 'S' and a 'step' value
# The function returns a list of slices from 'S' with a step of 'step'
def list_slice(S, step):
    return [S[i::step] for i in range(step)]

# Call the 'list_slice' function with the list 'C' and a step value of 3
# The function generates slices of 'C' with a step of 3 and returns a list of these slices
# Print the resulting list of slices
print(list_slice(C, 3))

## Alternative using List Comprehension
def split_list_nth(lst, n):
    """Split a list every Nth element"""
    return [lst[i:i+n] for i in range(0, len(lst), n)]

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

result = split_list_nth(my_list, n)
print(f"Original list: {my_list}")
print(f"Split every {n} elements: {result}")

## Alternative Using Generators Function
def split_list_nth_generator(lst, n):
    """Generator that yields chunks of size n"""
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

# Example usage
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n = 2

print(f"Original list: {my_list}")
print(f"Split every {n} elements:")
for chunk in split_list_nth_generator(my_list, n):
    print(chunk)
```

## Question 
Write a Python program to compute the difference between two lists.
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']


## Solution 
```python
# Import the 'Counter' class from the 'collections' module
from collections import Counter

# Define two lists 'color1' and 'color2' containing color names
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

# Create Counter objects 'counter1' and 'counter2' for each list to count the occurrences of color names
counter1 = Counter(color1)
counter2 = Counter(color2)

# Print the elements that are in 'counter1' but not in 'counter2' (Color1-Color2)
print("Color1-Color2: ", list(counter1 - counter2))

# Print the elements that are in 'counter2' but not in 'counter1' (Color2-Color1)
print("Color2-Color1: ", list(counter2 - counter1))
```