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

