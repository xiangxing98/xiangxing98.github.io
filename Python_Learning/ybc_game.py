import ybc_game

# 创建鼠标按下功能
def on_mouse_down():
    print('鼠标按下')

# 创建鼠标松开功能
def on_mouse_up():
    print('鼠标松开')

ybc_game.go()


import ybc_game

ybc_game.title('百变壮猿')

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
    bg.image = 'bg3'
    
ybc_game.go()
