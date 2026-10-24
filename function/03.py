#要区分 Modify（修改对象） 和 Reassign（重新赋值变量）

# Inner Function 可以访问 Outer Function 的 Variable
# Inner Function 可以 Reassign 自己的 Local Variable，但不能直接 Reassign Outer Function 的 Variable。
# 如果要 Reassign Outer Function 的 Variable，需要使用 nonlocal
def outer():
    v = 10
    def inner():
        v = 20
    inner()
    print(v)

outer() # 10

# 如果要reassign的话，要使用 nonlocal
# case1 : v 是 Outer Function 的 Local Variable
def outer2():
    v = 10
    def inner2():
        nonlocal v
        v = 20
    inner2()
    print(v)

outer2()

# 如果要 Reassign Outer Function 的 Variable，需要使用 nonlocal
# Case 2: val 是 Outer Function 的 Parameter
def outer3(arr, val):
    def helper():
        for i, n in enumerate(arr):

            # modify object
            arr[i] *= 2 

            # 用 nonlocal 来 reassign
            nonlocal val
            val *= 2

    helper()
    print(arr, val)

num = [2,4]
value = 5
outer3(num, value)