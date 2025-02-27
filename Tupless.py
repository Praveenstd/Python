# tuples are only to read not immutable
# tuples consists of duplicates
tupless = ("hi","hlo","huh","humm")
print(tupless.index("hi"))
print(tupless.count("hlo"))


# ---------------------------------------------
# Difference Between Mutable and Immutable in Python
# ---------------------------------------------

# Mutable: Objects whose values **can be changed** after creation.
# Immutable: Objects whose values **cannot be changed** after creation.

# ---------------------------------------------
# Key Differences:
# ---------------------------------------------
# - Mutable objects can be modified in-place (same memory location).
# - Immutable objects create a new object when modified.
# - Mutable objects are used when frequent changes are needed.
# - Immutable objects are used when stability and consistency are required.

# ---------------------------------------------
# Mutability of Common Data Types:
# ---------------------------------------------

# ✅ Mutable (Can be modified)
# ----------------------------
# - List (list)
# - Set (set)
# - Dictionary (dict)

# ❌ Immutable (Cannot be modified)
# --------------------------------
# - Tuple (tuple)
# - String (str)
# - Integer (int)
# - Float (float)
# - Frozenset (frozenset)

# ---------------------------------------------
# Examples of Mutable & Immutable Objects:
# ---------------------------------------------

# ✅ Example of a Mutable Object (List)
numbers = [1, 2, 3]  # List (Mutable)
numbers.append(4)  # Modifies the existing list
print(numbers)  # Output: [1, 2, 3, 4]

# ✅ Example of a Mutable Object (Dictionary)
person = {"name": "John", "age": 25}
person["age"] = 26  # Modifies the dictionary
print(person)  # Output: {'name': 'John', 'age': 26}

# ❌ Example of an Immutable Object (Tuple)
coordinates = (10, 20, 30)  # Tuple (Immutable)
# coordinates[0] = 40  # ❌ This will raise an error!

# ❌ Example of an Immutable Object (String)
text = "hello"
text = text + " world"  # Creates a new string (does NOT modify the original)
print(text)  # Output: "hello world"

# ---------------------------------------------
#
# --------------------------------
# Python Collections - Tuples
# --------------------------------
# A tuple is an ordered collection of elements.
# - Tuples **allow duplicate values**.
# - Tuples are **immutable** (cannot be changed after creation).
# - Elements in a tuple maintain **insertion order**.
# - Tuples are **faster** than lists due to immutability.
# - They can store **different data types** (int, str, list, etc.).

# --------------------------------
# Creating a tuple
tupless = ("hi", "hlo", "huh", "humm", "hi")  # Duplicate values are allowed
print("Original Tuple:", tupless)

# Finding the index of an element
print("Index of 'hi':", tupless.index("hi"))  # Returns the first occurrence index

# Counting occurrences of an element
print("Count of 'hi':", tupless.count("hi"))  # Returns how many times 'hi' appears

# Accessing elements (Indexing)
print("First Element:", tupless[0])  # Accessing by index
print("Last Element:", tupless[-1])  # Accessing last element

# Tuple Slicing
print("Sliced Tuple (1:3):", tupless[1:3])  # Returns elements from index 1 to 2

# --------------------------------
# Tuple Operations
# --------------------------------
# Concatenation (Joining two tuples)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Concatenated Tuple:", combined_tuple)

# Repeating a Tuple
repeated_tuple = tuple1 * 2  # Duplicates the tuple
print("Repeated Tuple:", repeated_tuple)

# Checking if an element exists
print("Is 'hlo' in tupless?", "hlo" in tupless)  # Returns True
print("Is 'bye' in tupless?", "bye" in tupless)  # Returns False

# --------------------------------
# Common Tuple Functions in Python:
# --------------------------------
# 1. tuple(iterable)      - Converts an iterable (e.g., list, set) into a tuple.
# 2. len(tuple)           - Returns the number of elements in the tuple.
# 3. tuple.index(value)   - Returns the index of the first occurrence of a value.
# 4. tuple.count(value)   - Returns the number of times a value appears in the tuple.
# 5. "value" in tuple     - Checks if an element exists in the tuple (returns True/False).
# 6. tuple1 + tuple2      - Concatenates two tuples.
# 7. tuple * n            - Repeats the tuple `n` times.
# 8. tuple[start:end]     - Slices a tuple (returns a subtuple).

# --------------------------------
# Important Notes:
# - Since tuples are **immutable**, they do not have methods like append(), remove(), or pop().
# - Use `dir(tuple)` to check all available methods.
# - Use `help(tuple.method_name)` for more details on a specific method.
# --------------------------------
