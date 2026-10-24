# 内部函数只能在外部函数内部调用
def outer():
    def inner():
        return "Hello"

    return inner()

print(outer())  # Hello

# print(inner())  # NameError


# 内部函数只能在外部函数内部调用, 除非透过return把内部函数传到外部
def outer2():
    def inner2():
        return "morning"
    return inner2

my_function = outer2()
print(my_function())
