# Looping

Loops are used to iterate over a sequence (list, tuple, dictionary, set, or string).

## For Loops

Iterating over a list:

```python
courses = ['Math', 'Physics', 'Chemistry', 'Biology']

for course in courses:
    print(course)
```

## Comparisons

You can use the `enumerate()` function to get the index while looping.

```python
for index, course in enumerate(courses):
    print(index, course)
```

## While Loops

Execute a set of statements as long as a condition is true.

```python
x = 0

while x < 10:
    print(x)
    x += 1
```

## Break and Continue

- **`break`**: Stops the loop.
- **`continue`**: Stops the current iteration and continues with the next.

```python
# Break example
for course in courses:
    if course == 'Chemistry':
        break
    print(course)

# Continue example
for course in courses:
    if course == 'Chemistry':
        continue
    print(course)
```
