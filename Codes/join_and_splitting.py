"""
# Join and Split

Methods to convert between strings and lists.

## Join (`join()`)

Returns a string in which the elements of a sequence (like a list) have been joined by a string separator.

## Split (`split()`)

Splits a string into a list where each word is a list item.
"""

courses = ['Math', 'Physics', 'Chemistry', 'Biology']

# Join elements with a comma and space
courses_str = ', '.join(courses)

print("Joined string:")
print(courses_str)
# Output: Math, Physics, Chemistry, Biology

# Split the string back into a list using the same separator
new_courses = courses_str.split(', ')

print("\nSplit back into list:")
print(new_courses)
# Output: ['Math', 'Physics', 'Chemistry', 'Biology']
