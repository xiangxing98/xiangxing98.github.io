import ybc_game

# 创建鼠标按下功能
def on_mouse_down():
    print('鼠标按下')

# 创建鼠标松开功能
def on_mouse_up():
    print('鼠标松开')

ybc_game.go()


import ybc_game
import random

ybc_game.title('百变壮猿')
bg_list = ["bg1", "bg2", "bg3", "bg4", "bg5"]
face_list = ["face1", "face2", "face3", "face4", "face5"]
hair_list = ["hair1", "hair2", "hair3", "hair4", "hair5"]
dress_list = ["dress1", "dress2", "dress3", "dress4", "dress5"]

bg = ybc_game.actor('bg1')
face = ybc_game.actor('face1', [400, 310])
hair = ybc_game.actor('hair1', [400, 318])
dress = ybc_game.actor('dress1', [400, 460])

def update():
    bg.draw()
    face.draw()
    hair.draw()
    dress.draw()

def on_mouse_down():
    # 修改背景角色的image属性
    bg.image = random.choice(bg_list)
    face.image = random.choice(face_list)
    hair.image = random.choice(hair_list)
    dress.image = random.choice(dress_list)
    
ybc_game.go()


# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   ybc_game.py
@Time    :   2023/12/10 20:25:03
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2021, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib



'''
import ybc_game
import random

ybc_game.title('百变背景')
ybc_game.size(600, 800)

bg = ybc_game.actor('bg1')
zy = ybc_game.actor('zy1', [300, 420])

bg_list = ['bg1', 'bg2', 'bg3', 'bg4', 'bg5']
zy_list = ['zy1', 'zy2', 'zy3', 'zy4', 'zy5']

def update():
    bg.draw()
    zy.draw()

# 按下鼠标，随机切换背景图片
def on_mouse_down():
    bg.image = random.choice(bg_list)

# 松开鼠标，随机切换壮猿图片
def on_mouse_up():
    zy.image = random.choice(zy_list)
    
ybc_game.go()

'''
