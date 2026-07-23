"""
# Type Casting

**Casting** is the process of converting one data type to another.

## Example: String to Integer

Converting string numbers to integers allows for mathematical operations.

## Single Line Casting

You can cast directly within expressions.
"""

num_1 = '100' # string
num_2 = '200' # string

# Without casting, + concatenates strings
print("Without casting:", num_1 + num_2) # Output: 100200

# Casting to integer
num1 = int(num_1)
num2 = int(num_2)

print("With casting:")
print(num1 + num2) 
# Output: 300

print("Single line casting:")
print(int(num_1) + int(num_2)) 
# Output: 300
