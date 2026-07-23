"""
# Sortings

Methods to sort and organize lists in Python.

## Sort and Reverse

- **`sort()`**: Sorts the list in ascending order (modifies the original list).
- **`reverse()`**: Reverses the order of the list (modifies the original list).
- **`sorted()`**: Returns a *new* sorted list (does not modify the original).

### Using sorted() function
Use this when you want to keep the original list unchanged.

## Useful Built-in Functions

- **`min()`**: Returns the smallest item.
- **`max()`**: Returns the largest item.
- **`sum()`**: Returns the sum of all items.
- **`len()`**: Returns the number of items.
"""

courses = ['Math', 'Physics', 'Chemistry', 'Biology']

# Sort in ascending order
courses.sort()
print("After sort():", courses) 

# Reverse the list
courses.reverse()
print("After reverse():", courses)

# Sort in descending order
courses.sort(reverse=True)
print("After sort(reverse=True):", courses)

# Using sorted() function
sorted_courses = sorted(courses)
print("New sorted list:", sorted_courses)

# Useful Built-in Functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Min:", min(numbers)) # Output: 1
print("Max:", max(numbers)) # Output: 10
print("Sum:", sum(numbers)) # Output: 55
print("Len:", len(numbers)) # Output: 10
