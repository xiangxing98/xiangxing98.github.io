# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   random.py
@Time    :   2020/03/28 20:50:56
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

import random

print("\n\t")
print("start test choice:")
foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))

print("\n\t")
print("start test slice:")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回  
print(slice) 
print(list) #原有序列并没有改变
             
print("\n\t")
print("start test uniform:")
print(random.uniform(10, 20))  
print(random.uniform(20, 10)) 
    
print("\n\t")
print("start test randint:")
print(random.randint(10, 20))  
print(random.randint(0, 1))

print("\n\t")
print("start test random:")
print(random.random()*1000)
print(random.random())

print("\n\t")
print("start test shuffle:")
li = range(1, 20)
print(random.shuffle(li))
print(li)
