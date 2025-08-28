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
