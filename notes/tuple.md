# Tuple

A **Tuple** is a collection which is ordered and **unchangeable** (immutable).

- **Mutable**: Can be changed (e.g., Lists)
- **Immutable**: Cannot be changed (e.g., Tuples)

## Mutable Example (List)

Lists can be modified after creation.

```python
list_1 = ['physics', 'chemistry', 'biology']
list_2 = list_1

print(list_1)
print(list_2)

# Changing the first element
list_1[0] = 'math'

print(list_1)
print(list_2)
# Notice list_2 also changed because they point to the same object
```

## Immutable Example (Tuple)

Tuples cannot be modified after creation.

```python
tuple_1 = ('physics', 'chemistry', 'biology')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Attempting to change an element will raise an error
# tuple_1[0] = 'math' 
# TypeError: 'tuple' object does not support item assignment
```
