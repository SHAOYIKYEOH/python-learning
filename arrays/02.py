# loop through arrays

arr = [1,2,3,4,5]

# by using index
for i in range(len(arr)):
    print(arr[i])

print('----------')

# without index
for i in arr:
    print(i)

# if we want both index and value
for i,n in enumerate(arr):
    print(i,n)

print('----------')

# loop through multiple array simultaneously
nums1 = [1,3,5]
nums2 = [2,4,6]
for i,n in zip(nums1,nums2):
    print(i,n)

# reverse
nums1.reverse()
print(nums1)

# sort the array
numberArr = [1,3,2,67,34,54]
numberArr.sort()
print(numberArr)
numberArr.sort(reverse = True)
print(numberArr)

nameArr = ["jack","bob","alice","chris"]
nameArr.sort()
print(nameArr)

# custom sort (by length)
nameArr.sort(key=lambda x:len(x))
print(nameArr)