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
