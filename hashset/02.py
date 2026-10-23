# initailize a hashset


# method 1 (pass in a list)
lists = [1,2,3,4,5]
mySet = set(lists)
print(mySet) 

mySet2 = set([8,8,8,8]) 
print(mySet2) # {8} (no duplicates)


# method 2 (set comprehension 推导式)
mySet3 = {i for i in range(5)}  # Use curly braces {} instead of square brackets []
print(mySet3)