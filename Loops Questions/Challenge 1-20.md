### Question 
You are given a number n, take input of n and print its multiplication table in a single line using for loop till n * 10. 

Examples:

Input: n = 5
Output: 5 10 15 20 25 30 35 40 45 50
Input: n = 6
Output: 6 12 18 24 30 36 42 48 54 60

### Answer
```python
number = int(input("Please Enter a Number "))

result = 0
for num in range(10):
    result += number
    print(result, end=" ")
```

### Question
You are given a string s, you need to print its characters at even indices (index starts at 0).

Examples:

Input: s = "Geeks"
Output: Ges
Explanation: The even indices characters are printed.
Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Explanation: The even indices characters are printed.

### Solution
```python
words = input("Please Enter The Word: ")
result = ""
for word in range(len(words)):
    if word % 2 == 0:
        result += words[word]
print(result)

# Alternative
result = words[::2]
print(result)
```

### Question
Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.

Example:

Input: x = 3
Output: 3 2 1 0
Explanation: Numbers in decreasing order from 3 are 3 2 1 0.
Input: x = 5
Output: 5 4 3 2 1 0
Explanation: Numbers in decreasing order from 5 are 5 4 3 2 1 0.

### Solution
```python
words = int(input("Please Enter The Word: "))
while words >= 0:
    print(words, end=" ")
    words -= 1
```

### Question 
Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
Note: Don't add a new line in the end.

Example :

Input: n1 = 9, n2 = 4
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  9 18 27 36 45 54 63 72 81 90
- 4  8 12 16 20 24 28 32 36 40
-----------------------------------------
= 5 10 15 20 25 30 35 40 45 50
Input: n1 = 6, n2 = 2
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  6 12 18 24 30 36 42 48 54 60
- 2  4  6  8 10 12 14 16 18 20
-----------------------------------------
= 4  8 12 16 20 24 28 32 36 40

### Solution
```python
n1 = int(input("Please Enter First Number: "))
n2 = int(input("Please Enter Second Number: "))

n3 = n1 - n2
result = 0
for  i in range(10):
    result += n3
    print(result, end=" ")
```

### Question
Given an integer n, write a program to print the square of size n using "*" character. 

Examples :

Input: n = 4
Output:
* * * *
*     *
*     *
* * * *
Explanation: It's a square! Each side contains n = 4 .
Input: n = 3
Output:
* * * 
*   *
* * *
Explanation: It's a square! Each side contains n = 3 .

### Solution
```python
n = int(input("Please Enter First Number: "))
for i in range(n):
    if i == 0 or i == n-1:  # first or last row
        print("* " * n)
    else:  # middle rows
        print("*" + " " * (2*n - 3) + "*")
```
### Question
Given an integer n,  write a program to print the square wall of size n using a single loop and string multiplication. 

Examples:

Input: n = 5
Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
Explanation: Its perfect square wall. 
Input: n = 4
Output:
* * * * 
* * * * 
* * * * 
* * * * 
Explanation: Its perfect square wall. 

### Solution
```python
n = int(input("Please Enter First Number: "))
for i in range(n):
        print("* " * n)
```

### Question
Given an integer n,  write a program to print the square wall of size n using nested loops. Try not to use String multiplication.

Examples:

Input: n = 5
Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
Explanation: Its perfect square wall. 
Input: n = 4
Output:
* * * * 
* * * * 
* * * * 
* * * * 
Explanation: Its perfect square wall. 

### Solution
```python
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

### Question
Given an integer n. Write a program to print the Right angle triangle wall. The length of perpendicular and base is n.  Use single loop and string multiplication.

Note: Print exactly single " " after "*". Print a new line after printing the triangle.

Examples:

Input: n = 4
Output:
* 
* * 
* * * 
* * * * 
Explanation: Length of perpendicular and base of triangle is 4 .
Input: n = 3
Output:
* 
* * 
* * * 
Explanation: Length of perpendicular and base of triangle is 3 .

### Solution
```python
num = int(input("Please enter a number: "))
for i in range(num):
    for j in range(i + 1):
        print("*", end=" ")
    print()
```

### Question
Given an integer n. Write a program to print the Right angle triangle. The length of the perpendicular and base is n.  

Examples :

Input: n = 9
Output:
*
* *
*   *
*     *
*       *
*         *
*           *
*             *
* * * * * * * * * 
Explanation: Length of perpendicular and base of triangle is 9.
Input: n = 4
Output:
*
* *
*   *
* * * *
Explanation: Length of perpendicular and base of triangle is 4.

### Solution
```python
n = int(input("Please enter a number: "))

for i in range(n):
    if i == 0:
        print("*")
    elif i == n -1:
         print("* " * n)
    else:
        print("*" + " " * (2 * i - 1) + "*")
```

### Question
Given an integer n. Write a program to print the inverted "Right angle triangle" wall. The length of the perpendicular and base is n.

Note: Use string multiplication for python.

Examples:

Input: n = 4
Output:
* * * * 
* * * 
* * 
*
Explanation: Length of perpendicular and base of triangle is 4 .
Input: n = 3
Output:
* * * 
* * 
*
Explanation: Length of perpendicular and base of triangle is 3 .

### Solution
```python
n = int(input("Please enter a number: "))
for i in range(n,0, -1):
    for j in range(i,0, -1):
        print("*", end="")
    print()
``` 

### Question 
Given an integer n find the sum of the first n natural number.

Examples:

Input: n = 10
Output: 55
Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.
Input: n = 5
Output: 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15.

### Solution
```python
n = int(input("Please Enter Number: "))
result = 0
for i in range(1, n + 1):
    result += i
print(result)
```

### Question 
Given an integer n, write a program to return the factorial of n. The Factorial of a number is the product of all the numbers from 1 to n.

Note: 0 factorial is equal to 1.

Example:

Input: n = 5
Output: 120
Explanation: 1 * 2 * 3 * 4 * 5 = 120
Input: n = 10
Output: 3628800
Explanation: 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800

### Soltion
```python
n = int(input("Please Enter Number: "))
result = 1
for i in range(1, n + 1):
    result *= i
print(result)
```

### Question
Given an integer n. Write a program to print all the divisors of n in a single line.

Examples:

Input: n = 12
Output: 1 2 3 4 6 12
Explanation: 12 is divisible by 1 2 3 4 6 12.
Input: n = 10
Output: 1 2 5 10
Explanation: 10 is divisible by 1 2 5 10.

### Solution
```python
n = int(input("Please Enter Number: "))
result =  []
for i in range(1, n + 1):
    if n % i == 0:
      result.append(str(i))

print(" ".join(result), end="")
```

### Question 
Given an integer n check if n is prime or not.
A prime number is a number that is divisible by 1 and itself only.

Note: Print "True" if n is prime, otherwise print "False".

Examples:

Input: n = 17
Output: True 
Explanation: 17 is  divisible by only 1 and 17. So it's a prime number.
Input: n = 56
Output: False
Explanation: 56 is divisible by 2, 4, 7.....etc. So its not a prime number.

### Solution
```python
n = int(input("Please Enter Number: "))

if n < 2:
    print(False)
else:
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)
``` 
### Question
Given an integer n. Write a program to find the first prime number greater than n.

Examples:

Input: n = 15
Output: 17
Explanation: 17 is next prime number.
Input: n = 7
Output: 11
Explanation: 11 is the prime number next to 7.

### Solution
```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # check divisors up to sqrt(num)
        if num % i == 0:
            return False
    return True

def next_prime(n):
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

# Example usage
n = int(input("Enter a number: "))
print("Next prime number is:", next_prime(n))
```
### Question 
write a program to calculate for fibonacci.

### Solution 
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Example usage
print(fibonacci(10))  # Output: 55
```