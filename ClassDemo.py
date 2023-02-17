# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/16

a = 10


def test(a):
    a = a + 1
    print(a)


def test2():
    a = 8
    b = a

    print(a)


test(3)
test2()

total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)

aa = 200
bb = 300


class AA:
    aa = aa + 1
    ccc = 55

    def funaa(self):
        # global ccc
        print(self.ccc)
        global bb
        bb = 33
        dd = 500
        aa = 111
        print(aa)
        print(self.aa)
        print(bb)

        def funbb():
            nonlocal dd
            print(dd)


AA().funaa()


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()



print("-------------------")


aaaa = 100
class AAAA:
    aaaa = aaaa + 1

    def Inter(self):
        global aaaa
        aaaa = aaaa + 10
        print(aaaa)
        print(self.aaaa)


AAAA().Inter()


import glob
print(glob.glob('*.py'))


import os

import sys
for aa in sys.path:
    print(aa)