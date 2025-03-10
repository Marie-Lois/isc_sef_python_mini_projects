def cel_to_fah(celsius):
    return (fahrenheit * 9/5) + 32
def fah_to_cel(fahrenheit):
    return (celsius - 32) * 5/9

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter a choice: "))

if choice == 1:
    celsius = float(int("Enter temperature in fahrenheit: "))
    fahrenheit = cel_to_fah(celsius)
    print("{}C is equal to {}F" .format (celsius, fahrenheit))
elif choice == 2:
    fahrenheit = float(int("Enter temperature in celsius: "))
    celsius = fah_to_cel(fahrenheit)
    print("{}F is equal to {}C" .format(fahrenheit, celsius))
    