# Strings support slicing, just like lists.
# 切片包含起始索引，不包含结束索引。
fruit = "apple"
print(fruit[0:2])  # ap

# Strings are immutable: their characters cannot be changed in place.
# 字符串是不可变的，不能直接修改某个位置的字符。
# fruit[0] = "A"  # Raises TypeError, not SyntaxError.

# Create a new string and assign it back to the variable.
# 创建一个新字符串，再让 fruit 指向它；原来的字符串没有被修改。
fruit = "A" + fruit[1:]
print(fruit)  # Apple


# ascii value
# ASCII Value（ASCII 码） 是计算机用来表示字符（Character）的数字编号。
print(ord('a'))
print(ord('b'))

# 如果我们用for loop 去 loop str
strs = "apple"
for i in strs:
    print(i) 
# output
# a
# p
# p
# l
# e
