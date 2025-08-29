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


Alternative 
lst = [1, 2, 3, 4, 5, 6, -7, 8, 9, -10]

# Remove duplicates just in case
unique_lst = list(set(lst))
unique_lst.sort()

second_largest = unique_lst[-2]
print("Second Largest:", second_largest)
```
