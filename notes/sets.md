# Sets

A **Set** is a collection which is unordered and unindexed.

## Creating a Set

```python
cs_courses = {'Math', 'Physics', 'Chemistry', 'Biology'}

print(cs_courses)
```

## Membership Test

Check if an item exists in the set:

```python
print('Math' in cs_courses)
```

## Set Operations

### Intersection
Returns a set that is the intersection of two other sets (items present in both).

```python
cs_courses = {'Math', 'Physics', 'Chemistry', 'Biology'}
art_courses = {'History', 'English', 'Math', 'Physics'}

print(cs_courses.intersection(art_courses))
```

### Difference
Returns a set containing the difference between two or more sets (items in the first set but not in the second).

```python
print(cs_courses.difference(art_courses))
```

### Union
Returns a set containing the union of sets (all items from both sets).

```python
print(cs_courses.union(art_courses))
```

## Creating Empty Collections

It is important to know the correct way to create empty collections in Python.

### Empty List
```python
empty_list = []
print(empty_list)
```

### Empty Tuple
```python
empty_tuple = ()
print(empty_tuple)
```

### Empty Set
**Note:** `empty_set = {}` creates an empty dictionary, not a set!

Correct way to create an empty set:
```python
empty_set = set()
print(empty_set)
```