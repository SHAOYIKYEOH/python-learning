# HashMap (Dictionary) in Python
# Stores data as key-value pairs.
# Keys must be unique.

# Method 1: Initialize a HashMap manually
myHashMap = {"bob": 1, "alice": 2}
print(myHashMap)  # {'bob': 1, 'alice': 2}


# Search / Access a value by its key
print(myHashMap["bob"])  # 1
# Alternatively, use the .get() method
print(myHashMap.get("bob"))  # 1


# Add a new key-value pair
myHashMap["jack"] = 33
print(myHashMap)
# {'bob': 1, 'alice': 2, 'jack': 33}


# we can modify the value thats mapped to a key
myHashMap["bob"] = 100
print(myHashMap["bob"])  # 100


# Check if a key exists (Membership Check)
print("alice" in myHashMap)  # True


# Delete a key which will also delete the value
myHashMap.pop("alice")
print(myHashMap)
# {'bob': 100, 'jack': 33}
