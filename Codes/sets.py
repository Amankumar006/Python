"""
# Sets

A **Set** is a collection which is unordered and unindexed.

## Creating a Set

## Membership Test

Check if an item exists in the set:

## Set Operations

### Intersection
Returns a set that is the intersection of two other sets (items present in both).

### Difference
Returns a set containing the difference between two or more sets (items in the first set but not in the second).

### Union
Returns a set containing the union of sets (all items from both sets).

## Creating Empty Collections

It is important to know the correct way to create empty collections in Python.

### Empty List
### Empty Tuple
### Empty Set

**Note:** `empty_set = {}` creates an empty dictionary, not a set!
"""

cs_courses = {'Math', 'Physics', 'Chemistry', 'Biology'}
print("CS Courses Set:", cs_courses)

# Membership test
print("Is 'Math' in cs_courses?:", 'Math' in cs_courses)

art_courses = {'History', 'English', 'Math', 'Physics'}
print("Art Courses Set:", art_courses)

# Intersection
print("Intersection:", cs_courses.intersection(art_courses))

# Difference
print("Difference:", cs_courses.difference(art_courses))

# Union
print("Union:", cs_courses.union(art_courses))

# Creating Empty Collections
empty_list = []
print("Empty list:", empty_list)

empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Correct way to create an empty set
empty_set = set()
print("Empty set:", empty_set)
