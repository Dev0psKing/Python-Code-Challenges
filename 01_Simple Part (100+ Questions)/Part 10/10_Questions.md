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

# Question 3
Write a function named print_right that takes a string named text as a parameter and prints the string with enough leading spaces that the last letter of the string is in the 40th column of the display.

```
                                Monty
                             Python's
                        Flying Circus
```

# Question 4
Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

## Output
```
Calling spruce(3) should print out

Sample output
a spruce!
  *
 ***
*****
  *
Calling spruce(5) should print out

Sample output
a spruce!
    *
   ***
  *****
 *******
*********
    *
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

# Question 6
Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

sentence = "it was a dark and stormy python"

## Output
print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python

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

# Question 8 
Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

## Output

How many items: 3
Item 1: 10
Item 2: 250
Item 3: 34
[10, 250, 34]


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

# Question 10
Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

## Sample output

Word: once
Word: upon
Word: a
Word: time
Word: upon
You typed in 4 different words