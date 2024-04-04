import math

n = float(input("Enter the number to which the square root is required: "))

if n >= 0:
    s = math.sqrt(n)
    print(f"Square root of that number is {s}")
else:
    s = math.sqrt(abs(n))
    print(f"Square root of that number is {s}i")
