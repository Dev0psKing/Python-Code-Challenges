
### Question 
Given two numbers a and b. The task is to find the GCD of  a and b.
The GCD of two numbers is the largest number that can divide both a and b perfectly.

Examples:

Input: a = 6, b = 9
Output: 3
Explanation: After 3 there is no number that can divide both 6 and 9 perfectly.
Input: a = 10, b = 15
Output: 5
Explanation: 5 is the greatest common divisor of 10 and 15.

### Solution 
```python
import math
#User function Template for python3
a = int(input())
b = int(input())

# Your code here
c = math.gcd(a,b)
print(c)

# using Alternative 

```

### Question 
Given two numbers a and b. The task is to find out their LCM.

Examples:

Input: a = 5, b = 10
Output: 10
Explanation: LCM of 5 and 10 is 10
Input: a = 14, b = 8
Output: 56
Explanation: LCM of 14 and 8 is 56

### Solution
```python
import math

def LCM(a,b):
    # Your code here
    c =math.lcm(a,b)
    return c
print(LCM(10,20))

# Alternatively using Brute force Method

def LCM(a, b):
    if a == 0 or b == 0:
        return 0   # convention: LCM with 0 is 0
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1
print(LCM(0, 8))   # 0
print(LCM(10, 20)) # 20
```

### Question 
Given a string s of single space-separated words. Capitalize the first letter of all words and count the number of the words in the string. Print the line and the number in separate lines with new line character at the end.

Examples:

Input: s = "welcome to the world of geeks"
Output: 
Welcome To The World Of Geeks
6
Input: s = "are you enjoying programming"
Output:
Are You Enjoying Programming
4 

### Solution
```python
s = input("Please enter a sentence ")
new = s.split()
capitalized = []
for word in new:
    capitalized.append(word.capitalize())
count = len(capitalized)
result = " ".join(capitalized)
print(result)
print(count)
```