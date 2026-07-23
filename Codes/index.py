"""
# Index & Enumeration

## Indexing (`index()`)

Returns the index of the first occurrence of a specified value in a list.

## Enumeration (`enumerate()`)

`enumerate()` allows you to loop over an iterable and keep track of the index of the current item.

### Basic Usage

### Specifying a Start Index

You can change the starting value of the index counter (default is 0).
"""

courses = ['Math', 'Physics', 'Chemistry', 'Biology']

print("Index of 'Chemistry':")
print(courses.index('Chemistry'))
# Output: 2

print("\nBasic Enumerate:")
for index, course in enumerate(courses):
    print(index, course)

print("\nEnumerate starting from 1:")
for index, course in enumerate(courses, start=1):
    print(index, course)
