# print("hello world!")

print("hello world!")
print("hello world!")
print("hello world!")

# 行与缩进
if True:
    print("true")
else:
    print("false")

# 多行语句
itme_one = "itme_one"
item_two = "item_two"
item_three = "item_three"
total = itme_one + \
        item_two + \
        item_three

total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

# 数字(Number)类型
# python中数字有四种类型：整数、布尔型、浮点数和复数。
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔), 如 True。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j


str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print('''hellorunoob''')

# input("\n\n按下 enter 键后退出。")

import sys

x = 'runoob';
sys.stdout.write(x + '\n')

x = "a"
y = "b"
# 换行输出
print(x)
print(y)
print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()



import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('argv:', argv)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path


