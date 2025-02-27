# Python Collections - Lists
# --------------------------------
# A list is an ordered collection of homogeneous or heterogeneous data types.
# - Lists allow duplicate values.
# - Lists are mutable (can be modified).
# - Lists maintain the insertion order.

# --------------------------------
# Daily Plan:
# - 2 hours Python
# - 2 hours C++
# - 2 hours Problem Solving
# - 1 hour Social Media Profile Work
# - 1 hour Project
# --------------------------------

# Creating a list of words (Strings)
words = ["praveen", "want", "to", "win", "life", "praveen"]

# Iterating through the list and printing each word
for word in words:
    print(word)

# Finding the length of the list
print("Length of words list:", len(words))  # Returns the number of elements in the list

# Checking if "praveen" exists in the list
print("Is 'praveen' in words list?", "praveen" in words)  # Returns True/False

# Modifying the first element of the list
words[0] = "kumar"
print("Updated words list:", words)

# Adding a new element to the list
words.append("he will win")
print("After appending:", words)

# Removing a specific element from the list
words.remove("kumar")
print("After removing 'kumar':", words)

# Inserting an element at a specific index
words.insert(1, "hlo")
print("After inserting 'hlo' at index 1:", words)

# Reversing the list
words.reverse()
print("After reversing words list:", words)

# Creating another list of games
games = ["pubg", "freefire", "ludo", "bgmi"]

# Reversing the list (NOTE: reverse() modifies the list in-place and returns None)
games.reverse()
print("After reversing games list:", games)

# Finding the index of an element
print("Index of 'hlo' in words list:", words.index("hlo"))

# Counting occurrences of an element
print("Count of 'praveen' in words list:", words.count("praveen"))

# --------------------------------
# Common List Functions in Python:
# --------------------------------
# 1. append(item)       - Adds an item to the end of the list.
# 2. extend(iterable)   - Extends the list by appending elements from an iterable.
# 3. insert(index, item) - Inserts an item at a specific index.
# 4. remove(item)       - Removes the first occurrence of an item.
# 5. pop(index)         - Removes and returns the item at the given index (default: last item).
# 6. clear()            - Removes all elements from the list.
# 7. index(item)        - Returns the index of the first occurrence of an item.
# 8. count(item)        - Returns the number of times an item appears in the list.
# 9. sort()             - Sorts the list in ascending order.
# 10. reverse()         - Reverses the elements of the list.
# 11. copy()            - Returns a shallow copy of the list.
# 12. len(list)         - Returns the number of elements in the list.
# 13. "item" in list    - Checks if an item exists in the list (returns True/False).
# 14. list(iterable)    - Converts an iterable (e.g., tuple, string, set) into a list.

# --------------------------------
# Notes:
# - Use `dir(list)` to check all available methods for lists.
# - Use `help(list.method_name)` for more details on a specific method.
# --------------------------------
