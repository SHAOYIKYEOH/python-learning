# Tuple in Python
# Similar to a List, but Tuple is immutable.
# Tuples are typically initialized using parentheses ().

# Method 1: Initialize a Tuple
myTuple = (1, 2, 3)
print(myTuple)  # (1, 2, 3)

# Tuples are immutable (cannot modify existing elements).
# myTuple[0] = 0  # TypeError


# Method 2: Access elements by index
print(myTuple[1])  # 2


# Method 3: Use a Tuple as a Dictionary (HashMap) Key
# A Tuple can be a Key if all its elements are hashable.

myHashMap = {
    (1, 2): 4,
    (2, 3): 5
}

print(myHashMap[(1, 2)])  # 4


# Method 4: Store a Tuple in a HashSet
# A Tuple can be added to a Set if it is hashable. On the other hand, lists are not hashable

hashSet = set()

hashSet.add((1, 2))

print((1, 2) in hashSet)  # True