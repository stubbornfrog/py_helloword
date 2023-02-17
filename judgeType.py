# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/16

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))


# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
class A:
    def f(self):
        return 'hello world'


class B(A):
    def f(self):
        return 'hello world'


print(type(A))
print(type(A()))
print(A)

print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)
print(isinstance(A, A))
print("-----------------------")

param1 = 1
print(param1 is True)

print("-----------------------")
# bool 是 int 的子类
print(issubclass(bool, int))

print("-----------------------")
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)
print(type(new_names))

print("-----------------------")
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
print(type(multiples))

for multiple in multiples:
    print(multiple)

print("-----------------------")
a = (x for x in range(1, 10))
print(type(a))
print(type(tuple(a)))

print("-----------------------")

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

print("-----------------------")



