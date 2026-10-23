# A set stores unique, hashable elements (no duplicates).
# set 存储不重复、可哈希的元素。

# Membership checks and insertion take O(1) constant time.
# 查找和插入的时间复杂度是 O(1)，

mySet = set()

# Add value.
mySet.add(1)
mySet.add(2)
mySet.add(3)

# Adding a duplicate does not change the set.
mySet.add(1)

print(mySet)  # {1, 2, 3} — element order is not guaranteed

# search a value in constant time
print(1 in mySet)  # True

# remove elements
mySet.remove(1)
print(1 in mySet) # False
