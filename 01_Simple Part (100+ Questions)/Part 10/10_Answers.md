# Question 1 
Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

## Output expected
```python
sentence = "it was a dark and stormy python"

print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python
```

## Solution
```python
def first_word(param):
     words = param.split()
     return words[0] if len(words) > 0 else ""

def second_word(param):
     words = param.split()
     return words[1] if len(words) > 1 else ""

def last_word(param):
     words = param.split()
     return words[-1] if len(words) > 0 else ""

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
```

# Question 2
Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

## Output
```python
# same characters m and m
print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False
```


## Solution
```python
def same_chars(a,b,c):
   a,b,c = str(a), int(b), int(c) 
   if b < 0 or c < 0 or b >= len(a) or c >= len(a):
        return False
   else:
      return  a[b] == a[c]
       
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
```

# Question 3
Write a function named print_right that takes a string named text as a parameter and prints the string with enough leading spaces that the last letter of the string is in the 40th column of the display.

```
                                Monty
                             Python's
                        Flying Circus
```

## Solution
```python
def print_right(text, width=40):
    print(text.rjust(width))

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
```

# Question 4
Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

## Solution
```python
def spruce(size):
    print("a spruce!")
    
    # Print the tree
    for i in range(size):
        spaces = " " * (size - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)
    
    # Print the trunk
    print(" " * (size - 1) + "*")

# Example calls
spruce(3)
spruce(5)
```

# Question 5 
Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

## Output

``` 
same characters m and m
print(same_chars("programmer", 6, 7)) # True

different characters p and r
print(same_chars("programmer", 0, 4)) # False

the second index is not within the string
print(same_chars("programmer", 0, 12)) # False
``` 

# Solution

```python 
def spruce(size):
    print("a spruce!")
    
    # Print the tree
    for i in range(size):
        spaces = " " * (size - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)
    
    # Print the trunk
    print(" " * (size - 1) + "*")

# Example calls 
spruce(3)
spruce(5)

```

# Question 6
Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

sentence = "it was a dark and stormy python"

## Output
print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python

# Solution 
```python
def first_word(sentence):
    new = sentence.split()
    return new[0]
def second_word(sentence):
    new = sentence.split()
    return new[1]
def last_word(sentence):
    new = sentence.split()
    return new[-1]

print(first_word("it was a dark and stormy python"))
print(second_word("it was a dark and stormy python"))
print(last_word("it was a dark and stormy python"))
```

# Question 7 
Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.

## Output
```
Index: 0
New value: 10
[10, 2, 3, 4, 5]
Index: 2
New value: 250
[10, 2, 250, 4, 5]
Index: 4
New value: -45
[10, 2, 250, 4, -45]
Index: -1
```
# Solution 
```python
my_list = [1, 2, 3, 4, 5]

while True:
    input_index = int(input("Please add input number "))
    new_value = int(input("Please add a value "))

    if input_index == -1:
        break

    try:
       print( my_list[input_index] =  new_value)

    except Error:
        print("incorrect statement" )
            
```

# Question 8 
Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

## Output

How many items: 3
Item 1: 10
Item 2: 250
Item 3: 34
[10, 250, 34]

# Solution 

```python
# Ask for the number of items
item = int(input("How many items: "))  
item_list = []

# Loop to collect input values
for i in range(1, item + 1):
    value = int(input(f"Item {i}: "))  
    item_list.append(value)

# Print the final list
print(item_list)

```

# Question 9
Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.

## Output
The list is now []
a(d)d, (r)emove or e(x)it: d
The list is now [1]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: r
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: x
Bye!

# Solution 

``` Python
# Write your solution here
my_list = []
counter = 0

print("The list is now []")


while True:
    add_list = input("a(d)d, (r)emove or e(x)it: ")
    if add_list == "d":
        counter += 1
        my_list.append(counter)
        print(f"The list is now {my_list}")

    elif add_list == "r":
        if my_list:
            counter -= 1
            my_list.pop()
            print(f"The list is now {my_list}")

    elif add_list == "x":
        print("Bye!")
        break

```
# Question 10
Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

## Sample output

Word: once
Word: upon
Word: a
Word: time
Word: upon
You typed in 4 different words

# Solution 

```Python 

word_list = []
counter = 0

while True:

    word = input("Word ").strip()
    

    if word in word_list:
        break

    word_list.append(word)
    counter += 1
   
   
print(f"You typed in {counter} different words")
    
```


