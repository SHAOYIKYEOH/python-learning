# while loops
z = 1
while z < 5:
    print(z)
    z +=1

print('-----------')

# for loops
for i in range(5):
    print(i)

print('-----------')

# for loops from 2-5
for a in range(2,6):
    print(a)

print('-----------')

# for loops (decrement)
for x in range(6,1,-1):
    print(x)

print('-----------')

# for loops (dict)
# 字典要用 字典[key]来取value
fruit_list = {"apple":"苹果", "orange":"橘子", "durian":"榴莲"}

for fruit_key in fruit_list:
    print(f'{fruit_key}的中文是{fruit_list[fruit_key]}')