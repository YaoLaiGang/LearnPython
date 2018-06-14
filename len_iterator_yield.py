#Python中的迭代器和生成器（使用yield的函数）
#迭代器常使用iter()为构造方法 next()为遍历方法

x = list(range(5))
it = iter(x)
for i in it:
    print(i)

#使用yield的函数称为迭代器生成器函数，这个函数的特点如下
#1、该函数返回一个迭代器，但调用时函数不会执行
#2、每依次访问该迭代器，函数就执行到yield的地方返回一个值，并暂停执行
#3、依次执行，函数也依次执行

def fibonacci(n):#需要检查N的合法性，此处省略
    a , b = 0 ,1
    for i in range(n):
        yield b #这是一个暂存点
        a , b = b , a + b

y = fibonacci(5)
type(y) #y是一个迭代器
for i in y:
    print(i)

#何时使用yield？ 当函数返回一个很大的LIST的时候，使用yield，把一个大的LIST分解成小的返回，以节省内存

