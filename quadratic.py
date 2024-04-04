import math



def solve_quadratic(a, b, c):
    # Calculate discriminant
    discriminant = b**2 - 4*a*c

    # Check if discriminant is positive, zero, or negative
    if discriminant > 0:
        # Two real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2*a)
        return root, root
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Get user input for coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
root1, root2 = solve_quadratic(a, b, c)
print(f"Root 1: {root1}, Root 2: {root2}")
