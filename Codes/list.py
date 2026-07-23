"""
# Lists

A **List** is a collection of items which is ordered and changeable.

## Creating and Accessing Lists

## Indexing and Slicing

Access specific items using their index.

- Positive Indexing
- Negative Indexing (from the end)
- Slicing (Range of indexes)
"""

courses = ['Math', 'Physics', 'Chemistry', 'Biology']

print(courses)        # Prints the entire list
print(len(courses))   # Prints the number of items: 4

# Positive Indexing
print(courses[0])   # First element: Math
print(courses[1])   # Second element: Physics
print(courses[3])   # Fourth element: Biology

# Negative Indexing (from the end)
print(courses[-1])  # Last element: Biology
print(courses[-2])  # Second last element: Chemistry

# Slicing (Range of indexes)
print(courses[0:2]) # Items from index 0 up to (but not including) 2
print(courses[1:])  # Items from index 1 to the end
print(courses[:2])  # Items from the start to index 2
