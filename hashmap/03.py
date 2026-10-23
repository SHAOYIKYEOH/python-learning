# loop through a hashmap

Hashmap = {"apple":10, "orange":20, "durian":100, "grape":80}

# Method 1: Iterate through keys (default behavior)
# Use the key to access its corresponding value
for key in Hashmap:
    print(key, Hashmap[key])

# Method 2: Iterate through values only
# .values() returns a view of all values
for value in Hashmap.values():
    print(value)

# Method 3: Iterate through key-value pairs (tuple unpacking)
# .items() returns a view of key-value pairs
for key, value in Hashmap.items():
    print(key, value)