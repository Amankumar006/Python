# Sortings

Methods to sort and organize lists in Python.

## Sort and Reverse

- **`sort()`**: Sorts the list in ascending order (modifies the original list).
- **`reverse()`**: Reverses the order of the list (modifies the original list).
- **`sorted()`**: Returns a *new* sorted list (does not modify the original).

```python
courses = ['Math', 'Physics', 'Chemistry', 'Biology']

# Sort in ascending order
courses.sort()
print(courses) 

# Reverse the list
courses.reverse()
print(courses)

# Sort in descending order
courses.sort(reverse=True)
print(courses)
```

### Using sorted() function
Use this when you want to keep the original list unchanged.

```python
sorted_courses = sorted(courses)
print(sorted_courses)
```

## Useful Built-in Functions

- **`min()`**: Returns the smallest item.
- **`max()`**: Returns the largest item.
- **`sum()`**: Returns the sum of all items.
- **`len()`**: Returns the number of items.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(numbers)) # Output: 1
print(max(numbers)) # Output: 10
print(sum(numbers)) # Output: 55
print(len(numbers)) # Output: 10
```