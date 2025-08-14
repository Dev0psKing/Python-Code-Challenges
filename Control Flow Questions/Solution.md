## Question 
Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

## Solution 
```python
result = []
for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)
print(result)
```
## Question 2
Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius

```python



```