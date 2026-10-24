# function
def myfunction(a,b):
    return a * b

print(myfunction(2,4))

# nested function
# inner function 
# 内部函数可以访问外部函数中定义的变量和参数。
# 外部函数不能直接访问内部函数中定义的局部变量。
def outer(a,b):
    c = "c"
    def inner():
        return a+b+c
    return inner()

print(outer("a","b"))

