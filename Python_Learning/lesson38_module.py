# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson38_module.py
@Time    :   2020/05/04 18:44:18
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
import random
from math import pi as math_pi

random_int = random.randint(1, 10)
random_choice = random.choice([1, 3, 5])
print(random_int, random_choice)
# 2 1

# 想知道random有哪些函数和变量，可以用dir()方法：
print(dir(random))
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
# 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence',
# '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect',
# '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi',
# '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
# '_urandom',
# '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate',
# 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate',
# 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed',
# 'setstate',
# 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# 如果你只是用到random中的某一个函数或变量，也可以通过from...import...指明：
# from math import pi
# print (pi)

# 为了便于理解和避免冲突，你还可以给引入的方法换个名字：
# from math import pi as math_pi
print(math_pi)
# 3.141592653589793

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson38_module.py
'''
