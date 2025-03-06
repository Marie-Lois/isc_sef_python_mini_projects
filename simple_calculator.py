def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


def Multiply(a, b):
    return a * b


def  Division(a, b):
    if b == 0:
        print("No division by zero")
    else:
        return a / b


def Modulus(a, b):
    if b == 0:
        print("No division by zero")
    else:
        return a % b

    
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd Number: "))

print("1. Sum")
print("2. Difference")
print("3. Product")
print("4. Quotient")
print("5. Remainder")

operation = int(input("Enter an operation: "))

if operation == 1:
    sum = addition(number1, number2)
    print("Sum= {}" .format (sum))
elif operation == 2:
    Difference = subtract(number1, number2)
    print("Difference= {}" .format(Difference))

elif operation == 3:
    product = Multiply(number1, number2)
    print("Product= {}" .format(product))

elif operation == 4:
    quotient = Division(number1, number2)
    print("Quotient= {}" .format(quotient))

elif operation == 5:
    remainder = Modulus(number1, number2)
    print("Remainder= {}" .format(remainder))

else: print("Invalid operator")
