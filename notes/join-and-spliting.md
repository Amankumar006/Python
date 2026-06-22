# Join and Split

Methods to convert between strings and lists.

## Join (`join()`)

Returns a string in which the elements of a sequence (like a list) have been joined by a string separator.

```python
courses = ['Math', 'Physics', 'Chemistry', 'Biology']

# Join elements with a comma and space
courses_str = ', '.join(courses)

print(courses_str)
# Output: Math, Physics, Chemistry, Biology
```

## Split (`split()`)

Splits a string into a list where each word is a list item.

```python
# Split the string back into a list using the same separator
new_courses = courses_str.split(', ')

print(new_courses)
# Output: ['Math', 'Physics', 'Chemistry', 'Biology']
```