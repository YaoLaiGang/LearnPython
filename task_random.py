#Python中猜数字小游戏
import random
x = random.choice(range(100))
user = int(input('请输入一个0-99的数字'))
while x != user:
    if x > user:
        user = int(input('太小了，请重新输入\n'))
    else :
        user = int(input('太大了，请重新输入\n')) 
else:
    print('正确数字是',user)
