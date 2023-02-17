# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/16
# /用来指明他前面的函数形参必须使用位置参数。
# *用来指明他后面的函数形参必须为关键字参数的形式


def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


a = 1
print(id(a))
change(a)
print(a)

print("-----------------------")


# 可写函数说明
def printinfo(name, age=35):
    # "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")
printinfo("runoob")

print("------------------------")


# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)
print("------------------------")


def f(a, b, *, c):
    return a + b + c


print(f(1, 2, c=3))
print("------------------------")


xx = lambda aa: aa + 10
print(xx(5))
print("------------------------")
#返回匿名函数

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))