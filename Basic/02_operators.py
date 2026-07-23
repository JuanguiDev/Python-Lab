# Operators

## Boolean
print(True)
print(False)

## Arithmetic operators
a = 2
b = 3

print(a + b)  # Addition (5)
print(a - b)  # Subtraction (-1)
print(a * b)  # Multiplication (6)
print(a / b)  # Division (0.666)
print(a % b)  # Modulus (2)
print(a // b) # Floor division (0)
print(a ** b) # Exponentiation (8)

# Comparison Operators
print(3 > 2)  # True
print(3 >= 2) # True
print(3 < 2)  # False
print(2 < 3)  # True
print(2 <= 3) # True
print(3 == 2) # False
print(3 != 2) # True

# Logical Operators
print(3 > 2 and 4 > 3)  # True
print(3 > 2 and 4 < 3)  # False
print(3 < 2 and 4 < 3)  # False
print(3 > 2 or 4 > 3)   # True
print(3 > 2 or 4 < 3)   # True 
print(3 < 2 or 4 < 3)   # False
print(not 3 > 2)        # False
print(not True)         # False
print(not False)        # True
print(not not True)     # True
print(not not False)    # False