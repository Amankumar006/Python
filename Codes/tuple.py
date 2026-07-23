"""
# Tuple

A **Tuple** is a collection which is ordered and **unchangeable** (immutable).

- **Mutable**: Can be changed (e.g., Lists)
- **Immutable**: Cannot be changed (e.g., Tuples)

## Mutable Example (List)

Lists can be modified after creation.

## Immutable Example (Tuple)

Tuples cannot be modified after creation.
"""

# Mutable Example (List)
list_1 = ['physics', 'chemistry', 'biology']
list_2 = list_1

print("--- Mutable Example (List) ---")
print("Initial list_1:", list_1)
print("Initial list_2:", list_2)

# Changing the first element
list_1[0] = 'math'

print("Modified list_1:", list_1)
print("list_2 (reflects change):", list_2)

# Immutable Example (Tuple)
tuple_1 = ('physics', 'chemistry', 'biology')
tuple_2 = tuple_1

print("\n--- Immutable Example (Tuple) ---")
print("Initial tuple_1:", tuple_1)
print("Initial tuple_2:", tuple_2)

# Attempting to change an element will raise an error
try:
    tuple_1[0] = 'math'
except TypeError as e:
    print(f"Error raised as expected: {e}")
