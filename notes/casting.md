# Type Casting

**Casting** is the process of converting one data type to another.

## Example: String to Integer

Converting string numbers to integers allows for mathematical operations.

```python
num_1 = '100' # string
num_2 = '200' # string

# Without casting, + concatenates strings
# print(num_1 + num_2) # Output: 100200

# Casting to integer
num1 = int(num_1)
num2 = int(num_2)

print(num1 + num2) 
# Output: 300
```

## Single Line Casting

You can cast directly within expressions.

```python
print(int(num_1) + int(num_2)) 
# Output: 300
```