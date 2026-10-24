# we can convert strings into number or number to strings
print(int("123")+int("123"))
print(str(123)+str(123))

# we can combine strings together with custom delimitor
# join() 会把 List 里面的 String Elements 连接起来，并返回一个新的 String Object
strings = ['a','b','x','y']
print(strings)           # ['a', 'b', 'x', 'y']

# 重要区别：.join() 不会改变原本的 List，而是创建一个新的 String。
print("".join(strings))  # abxy
print(",".join(strings)) # a,b,x,y

# sort() 只会modify 不会return 一个新的list
nameList = ["jack","bob","alice","tom"]
result = nameList.sort()
print(result) # None
print(nameList) # ['alice', 'bob', 'jack', 'tom']


# sorted() 不会modify，而是会return 一个新的list 
nameList2 =  ["jack","bob","alice","tom"]
result2 = sorted(nameList2)
print(result2) # ['alice', 'bob', 'jack', 'tom']

print(sorted('i_will_break_into_a_sorted_list'))
print("".join(sorted('i_will_not_break_into_a_sorted_list'))) # _______aabdeeiiiiklllnnooorrssttttw

# print("i_will_not_break_into_a_sorted_list".sort()) this wont work. str 没有sort 这个method
