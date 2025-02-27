# Creating a dictionary of country capitals
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# Accessing dictionary elements
print(capitals["USA"])
print(capitals.get("Japan"))  # Returns None if key is not found

# Checking if a key exists
if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# Updating dictionary elements
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})  # Updating an existing key

# Removing elements from dictionary
capitals.pop("China")  # Removes the key-value pair for "China"
capitals.popitem()  # Removes the last inserted item
capitals.clear()  # Clears the dictionary

# Iterating through dictionary keys
keys = capitals.keys()
for key in capitals.keys():
    print(key)

# Iterating through dictionary values
values = capitals.values()
for value in capitals.values():
    print(value)

# Iterating through dictionary items (key-value pairs)
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
