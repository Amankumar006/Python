# Index & Enumeration

## Indexing (`index()`)

Returns the index of the first occurrence of a specified value in a list.

```python
courses = ['Math', 'Physics', 'Chemistry', 'Biology']

print(courses.index('Chemistry'))
# Output: 2
```

## Enumeration (`enumerate()`)

`enumerate()` allows you to loop over an iterable and keep track of the index of the current item.

### Basic Usage

```python
for index, course in enumerate(courses):
    print(index, course)
```

**Output:**
```text
0 Math
1 Physics
2 Chemistry
3 Biology
```

### Specifying a Start Index

You can change the starting value of the index counter (default is 0).

```python
for index, course in enumerate(courses, start=1):
    print(index, course)
```

**Output:**
```text
1 Math
2 Physics
3 Chemistry
4 Biology
```
