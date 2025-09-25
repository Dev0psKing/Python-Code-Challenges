
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