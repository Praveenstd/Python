# Python Collections - Sets
# --------------------------------
# A set is an unordered collection of unique elements.
# - Sets do NOT allow duplicate values.
# - Sets do NOT maintain order like lists.
# - Sets are **mutable** (you can add/remove elements), but **individual elements are immutable**.
# - Elements in a set must be hashable (e.g., strings, numbers, tuples).

# --------------------------------
# Creating a set
uno = {"earth", "sun", "mars", "jupiter"}

# Iterating through the set (unordered output)
for planet in uno:
    print(planet)

# Finding the length of the set
print("Length of the set:", len(uno))  # Returns the number of elements in the set

# Checking if an element exists in the set
print("Is 'sun' in uno set?", "sun" in uno)  # Returns True
print("Is 'pluto' in uno set?", "pluto" in uno)  # Returns False

# Adding elements to the set
uno.add("pluto")  # Adds 'pluto' to the set
print("After adding 'pluto':", uno)

# Removing elements from the set
uno.remove("mars")  # Removes 'mars' from the set (throws an error if element is not found)
print("After removing 'mars':", uno)

# Discarding an element (safe removal, does NOT throw an error if element is not found)
uno.discard("venus")  # No error if 'venus' is not in the set
print("After discarding 'venus':", uno)

# Popping a random element (since sets are unordered, we don't know which will be removed)
removed_element = uno.pop()
print("Removed element:", removed_element)
print("After popping an element:", uno)

# Clearing the entire set
uno.clear()
print("After clearing the set:", uno)

# --------------------------------
# Common Set Functions in Python:
# --------------------------------
# 1. add(item)          - Adds an item to the set.
# 2. remove(item)       - Removes an item from the set (throws an error if item is not found).
# 3. discard(item)      - Removes an item from the set (does NOT throw an error if item is missing).
# 4. pop()              - Removes and returns a random item from the set.
# 5. clear()            - Removes all elements from the set.
# 6. len(set)           - Returns the number of elements in the set.
# 7. "item" in set      - Checks if an item exists in the set (returns True/False).
# 8. set1.union(set2)   - Returns a new set with elements from both sets.
# 9. set1.intersection(set2) - Returns a new set with elements common to both sets.
# 10. set1.difference(set2) - Returns a new set with elements in set1 but not in set2.
# 11. set1.symmetric_difference(set2) - Returns elements in either set1 or set2 but not both.
# 12. set1.issubset(set2)  - Checks if set1 is a subset of set2.
# 13. set1.issuperset(set2) - Checks if set1 is a superset of set2.
# 14. set(iterable)      - Converts an iterable (e.g., list, tuple) into a set.

# --------------------------------
# Notes:
# - Use `dir(set)` to check all available methods for sets.
# - Use `help(set.method_name)` for more details on a specific method.
# --------------------------------
