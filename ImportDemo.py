# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/16

import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)
print('命令行参数如下:')
for path in sys.path:
    print(path)

