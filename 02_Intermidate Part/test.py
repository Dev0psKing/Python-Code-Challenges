celsius = int(input("Enter Celsius: "))
fahrenheit= int(input("Enter Fahrenheit: "))

formularCelsius = (celsius * 9/5) + 32
formularFahrenheit = (fahrenheit - 32) * 5/9
print(f"{celsius}°C is {int(formularCelsius)} in Fahrenheit")
print(f"{fahrenheit}°F is {int(formularFahrenheit)} in Celsius")