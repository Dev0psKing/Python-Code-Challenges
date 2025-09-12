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
```