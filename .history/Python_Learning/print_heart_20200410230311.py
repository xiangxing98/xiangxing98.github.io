print('''
   ***                 ***
 *********           *********
************       ************
*************     *************
**************   **************
*************** ***************
 *******    *** ***    *******
  ******     *****     ******
   ******     ***     ******
   ******     ***     ******
     ******    *     ******
       ******  *   ******
         **************
           **********
             ******
               ***
                *

''')

print('''
    去他个鸟命！
    我命由我，不由天！
    是魔是仙，我自己决定！
    靠'自己'
''')

# 穿上单引号、双引号、三引号黄袍的内容就是字符串，无论引号里面内容是中文、英文、法文、数字、符号、甚至是火星文
movie = '美国队长2'
name = 'The Winter Soldier'
price = "7.14"
word = '''≡(▔﹏▔)≡'''
print(movie)
print(name)
print(price)
print(word)

say = '我们强者就该无所畏惧。'
print(say)
say1 = '那你为什么要跑？'
print(say1)

# float
print(0.35+0.11)
# 0.45999999999999996
# 呀？ 怎么不是0.46呢，而是一个比0.46小的数字？
# 这是因为Python计算浮点数时，会把0.35与0.11转换成二进制数 【
# 江湖秘籍：二进制数由0和1表示，逢2进1】

# 二进制转换
# 0.35（十进制） = 0.010110011001100110011001100110011001100110011001100111（二进制）
# 0.11（十进制）= 0.00011100001010001111010111000010100011110101110000101001（二进制）
# 在这个十进制转换二进制过程中，产生了误差，这样就造成了我们与结果的误差。
# 然后，这两个二进制数字相加后，在将得到的二进制结果转换成十进制小数。

hero = '美国队长'
title = '漫威漫画'
action = '取材于'
print(hero+action+title)

hero = '美国队长'
title = '漫威漫画'
action = '编写'
place = '于'
print(hero+place+title+action)

name = '美国队长'
num = 2
print(type(name))
print(type(num))

# 数据转换的方法有3个: str() ，int()，float()
# Str()函数可以帮助我们解决刚才问题，它可以将其他类型的数据变换成str类型。
name = '美国队长'
num = 2
print(name+str(num))

name = '美国队长'
add = '的'
height = '身高'
gaodu = 198
print(name+add+height+str(gaodu))

num1 = '3'
num2 = '6'
print(int(num1)+int(num2))

height = 198.2
weight = 97
age = '30'
print(float(height))
print(float(weight))
print(float(age))

num1 = 1
num2 = 2
name1 = '囚犯'
name2 = 'CA'
word1 = '你有什么能力来带我们出去?'
word2 = '我揍了希特勒200多次'
symbol = ':'

print(str(num1) + name1 + symbol + word1)
print(str(num2) + name2 + symbol + word2)

name = '美国队长'
num = '2.5'
word = '该片于2014年4月4日在北美与中国同步上映。'

print(name + str(int(float(num))) + word)


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
