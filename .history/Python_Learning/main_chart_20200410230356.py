import time, random
from kkb_robot import send_message

feature_text = '''
大家好！我是您的聊天机器人小K。
我有问必答，有人会问我“今天深圳天气怎么样？”，也有人问我“您喜欢我吗？”
快来问我问题呀，欢迎来撩！
'''

print(feature_text)
user1 = '>你是谁~'


time.sleep(1)
print(user1)
userid = str(random.randint(1, 1000000000000000000000))
jsrobot1 = send_message(userid, user1)
print(jsrobot1)

time.sleep(1)

print('''
再来问我点啥吧！我把我知道的都告诉您，嘻嘻！
''')
user2 = '>天气'
print(user2)
time.sleep(1)
jsrobot1 = send_message(userid, user2)
print(jsrobot1)
time.sleep(1)


user3 = '>北京'


jsrobot1 = send_message(userid, user3)
print(user3)
time.sleep(1)
print(jsrobot1)
time.sleep(1)
print('\n我走啦，拜拜！')
