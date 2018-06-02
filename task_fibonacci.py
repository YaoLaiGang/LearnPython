#用Python实现菲波那切数列并输出，小练手
a , b = 0 , 1
for i in range(10):
    print(b)
    a , b = b , a+b
#使用LIST同样可以解决问题
n = int(input('请输入一个整数'))
list1 = [1,1]
while n>0:
    list1.append(list1[-1]+list1[-2])
    n-=1
print(list1)