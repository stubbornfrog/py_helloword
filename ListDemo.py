# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/16

# 当做栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)

print("---------------------------")
# 当做队列使用
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

print("---------------------------")

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])
cc = range(3)
print(type(cc))
print(tuple(cc))
print([vec1[i] * vec2[i] for i in range(len(vec1))])
print([str(round(355 / 113, i)) for i in range(1, 6)])
print("---------------------------")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
print([[row[i] for row in matrix] for i in range(4)])
# 上下等价
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
print("---------------------------")

tupleaa = 12345, 54321, 'hello!'
tupleab = (12345, 54321, 'hello!')
tupleac = [12345, 54321, 'hello!']
tuplead = {12345, 54321, 'hello!'}
print(type(tupleaa))
print(type(tupleab))
print(type(tupleac))
print(type(tuplead))
print('hello!' in tupleac)
print("---------------------------")


print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print(type({x for x in (2, 4, 6)}))
print({x for x in (2, 4, 6)})
print(type({x: x**2 for x in (2, 4, 6)}))
print({x: x**2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))
print("---------------------------")

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print(tuple(range(1, 10, 2)))