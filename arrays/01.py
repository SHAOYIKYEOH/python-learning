# arrays (called lists in python)

arr = [1,2,3,4,5]
print(arr)

arr.pop()
print(arr)

arr.append(9)
print(arr)

arr.insert(0,8) # insert(index, value)
print(arr)

# Big O notation describes how time complexity grows as input size n grows.
# Python list:
# Access by index: O(1)
# Search by value: O(n) ## 也就是说 如果只是单纯的 for loop 的话 它循环的次数就和arr 的长度一样。完整遍历时，循环次数等于 arr 的长度 n
# Iterate over all elements: O(n)


# sublists(aka slicing)
arr2 = [1,2,3,4,5]
print(arr2[1:4])


# when we are indexing an array, -1 is not out of bound 
print(arr2[-1])

# initialize array of size n with default value of 1
n = 5
arr3 = [1] * 5
print(arr3)
print(len(arr3))

# unpacking
# The number of variables on the left must match the number of elements on the right.
x,y,z = [9,8,7]
print(x,y,z)
print(x)
print(y)
print(z)