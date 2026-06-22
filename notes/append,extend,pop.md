# List Methods: Append, Extend, Pop

Common methods to modify lists.

## Adding Elements

- **`append()`**: Adds a single item to the end of the list.
- **`extend()`**: Adds all elements from another iterable (list, tuple, string) to the end.
- **`insert()`**: Adds an element at a specified index position.

```python
courses = ['Math', 'Physics']

# Append
courses.append('Computer Science')
print(courses)
# Output: ['Math', 'Physics', 'Computer Science']

# Extend
courses.extend(['Art', 'History'])
print(courses)
# Output: ['Math', 'Physics', 'Computer Science', 'Art', 'History']

# Insert
courses.insert(0, 'Biology') # Insert at index 0
print(courses)
# Output: ['Biology', 'Math', 'Physics', 'Computer Science', 'Art', 'History']
```

## Removing Elements

- **`remove()`**: Removes the first occurrence of a logical value.
- **`pop()`**: Removes and returns an element at a specific index (default is the last one).

```python
# Remove a specific value
courses.remove('Math')
print(courses)

# Pop the last element
last_popped = courses.pop()
print(last_popped) # Output: History

# Pop from a specific index
first_popped = courses.pop(0)
print(first_popped) # Output: Biology
```
