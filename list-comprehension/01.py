# initialize array （初始化数组／列表）
n = 5
arr = [1]*5
print(arr)

print('------------')

# list comprehension_1 （列表推导式）
arr2 = [i for i in range(5)]
print(arr2)

print('------------')

# list comprehension_2 （列表推导式）
arr3 = [i+i for i in range(5)]
print(arr3)

# list comprehension_3 （列表推导式）(2d lists)
arr4 = [[0]*4 for i in range(5)] # we dont have to use variable i here
print(arr4)