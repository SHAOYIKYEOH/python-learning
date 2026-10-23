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

