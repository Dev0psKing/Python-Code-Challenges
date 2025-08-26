## Question 
Write a Python program to sum all the items in a list.

## Solution 
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

## Question
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

## Question 
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

## Question 
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


# Question 
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



listItem =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sort_list = sorted(listItem, key=lambda x: x[1])

print(sort_list)