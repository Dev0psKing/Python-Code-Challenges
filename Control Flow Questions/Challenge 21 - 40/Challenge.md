
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
