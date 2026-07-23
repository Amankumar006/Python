"""
# Looping

Loops are used to iterate over a sequence (list, tuple, dictionary, set, or string).

## For Loops

Iterating over a list:

## Comparisons

You can use the `enumerate()` function to get the index while looping.

## While Loops

Execute a set of statements as long as a condition is true.

## Break and Continue

- **`break`**: Stops the loop.
- **`continue`**: Stops the current iteration and continues with the next.
"""

courses = ['Math', 'Physics', 'Chemistry', 'Biology']

print("--- For Loop ---")
for course in courses:
    print(course)

print("\n--- Enumerate ---")
for index, course in enumerate(courses):
    print(index, course)

print("\n--- While Loop ---")
x = 0
while x < 10:
    print(x)
    x += 1

print("\n--- Break Example ---")
for course in courses:
    if course == 'Chemistry':
        break
    print(course)

print("\n--- Continue Example ---")
for course in courses:
    if course == 'Chemistry':
        continue
    print(course)
