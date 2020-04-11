import time

print('如果你想拥有读心术，那选择X教授')

time.sleep(2)

print('如果你想干扰地球磁场，那选择万磁王')

time.sleep(2)

print('如果你想急速自愈能力，野兽般的感知能力，那选择金刚狼')

time.sleep(2)

print('如果你想拥有拥有念力移位和心电感应，那选择凤凰女')

time.sleep(2)

print('如果你想拥有拥有能随意控制气候的能力，那选择暴风女')

time.sleep(2)

print('那么，如果让你来选择的话，你想选择哪个人物？')

time.sleep(2)

print('请在以下六个选项【1 X教授 ；2 万磁王；3 金刚狼 ；4 凤凰女；5 暴风女 ；】中，选择你最想成为的人物吧！')

time.sleep(3)

answer = input('请将对应数字输入在冒号后： ')

if answer == '1':
    print('我是教授，通过其能力剥夺并控制他人的思维同时操纵他人的行动。')
    time.sleep(3)

elif answer == '2':
    print('我X万磁王，通过干扰地球磁场达到飞行的能力。')
    time.sleep(3)

elif answer == '3':
    print('我是金刚狼，天生双臂长有可伸出体外的利爪')
    time.sleep(3)

elif answer == '4':
    print('我是凤凰女，预知未来，并能抗拒他人的精神攻击。')
    time.sleep(3)

elif answer == '5':
    print('我是暴风女，被称作天气女神。')
    time.sleep(3)


# 为钱包赋值
money = 1000

# 条件：如果有1000块钱以上(包含1000块)，就去吃日料
if money>=1000:

# 结果：显示‘金刚狼带凤凰女去吃日料’的结果
print('金刚狼带凤凰女去吃日料')
# IndentationError: expected an indented block （缩进错误）