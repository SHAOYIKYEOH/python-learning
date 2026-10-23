# Division is decimal by default
a = 5/2
print(a)

# Double slash rounds down
# and 它会往下取 1--2--(2.5)--3--4--5
b = 5//2
print(b)

c = -3//2
print(c)

# int(-3//2) to 向上取
d = int(-3/2)
print(d)

# math helpers
import math

print(math.floor(3//2)) # 1
print(math.ceil(3//2)) # 2
print(int(math.pow(2,3))) # 8
print(int(math.sqrt(25))) # 5