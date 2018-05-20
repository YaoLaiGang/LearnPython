#encoding utf-8
# 试题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，
# 又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想吃时，只剩下一个桃子了。求第一天共摘多少个桃子。（优雅的方法：迭代法）
day=9
x=1
while day>0:
	x=(x+1)*2
	day-=1;
print("总共有:",x)
#看程序， 写结果
def foo(s):
 	if s=="":
 		return s
 	else:
 		return foo(s[1:])+s[0]
print (foo("Happy New Year."))
#看程序，写结果
arr=[2,4,1,3,6,8]
for e in arr:
	index=0
	if e%2==0:
		arr.pop(index)
		index+=1
print (arr)
#猜数字游戏，预设一个0-9之间的整数，让用户输入数字，如果过大就
#显示“太大”，小于该值就显示“太小”，知道猜中该数，显示“恭喜，猜中了”
import random
s=input("请输入一个整数")
a=int(s)
b=random.randint(0,100)
flag=0
while flag==0:
	if a==b:
		print("恭喜！你猜中了！")
		flag=1
	if a>b:
		a=int(input("太大"))
	if a<b:
		a=int(input("太小"))
