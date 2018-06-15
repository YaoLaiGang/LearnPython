#Python函数的用法
#1. 函数定义
def 函数名 (参数列表):
    #函数体
    pass

def hello():
    print('hello world!')
hello()

#计算面积
def area(width,height):
    return width*height

def print_welcome(name):
    print("welcome",name)

print_welcome('laigang')
w , h = 4,5
print(w,h,area(w,h))

#需要注意的是，Python中类型属于对象，而变量本身并没有类型，所以参数并没有声明其类型
'''
可更改变量 不可更改变量
由于两者在传递参数的时候的底层实现不同，故需要区分
mutable : list dict 使用引用传递，函数内修改函数外也受影响
immutable : String tuples numbers 使用值传递，栈空间自动开辟副本

'''

#尝试修改number
def changeInt(a):
    a = 10

b = 2
changeInt(b)
print(b)

#修改LIST
def changeList(myList):
    myList.append(list(range(0,5,2)))
myList = [10,20,30]
changeList(myList)
print(myList)

'''
参数分类
必须参数：必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
关键字参数：在使用的时候指定‘参数名 = value ' 这样可以变更参数顺序
默认参数：这个语法在c++中也存在，在参数中指定默认值，比如age = 20,当用户不指定改参数的时候，采用默认值
不定长参数:固定格式 func（arg1,*vartuple）顾名思义，当参数加了*，它就会接受多个参数，并打包成元组
'''
#关键字参数,默认参数
def printme(str1,age = 30):
    print(str1)
printme(age=50,str1='30')
printme('test')

#不定长参数
def printinfo(arg1,*vartuple):
    #打印任何传入的参数
    print(arg1)
    for var in vartuple:
        print(var,end = '^^^')
printinfo('测试',2,3,54,4,6,3,5,7)

#注意 *后的参数必须使用关键字参数指定,否则会报错，*可以单独出现
def f(a,b,*,c):
    return a+b+c
f(1,2,c=6)

'''
匿名函数 lambda表达式
注意，lambda只是一个表达式，不是一个代码块，只能写有限的语法
特殊的是lambda拥有自己的命名空间，而且无法访问自己参数外的或全局命名空间的变量
'''

#lambda [arg1[,arg2,……,argn]]:expression

sum = lambda arg1,arg2 : arg1+arg2

print(sum(20,30))

'''
return 
这个就老生常谈了，从函数诞生之日return就是一个逃不掉的话题，Python也不例外
只需要说明一点，当不指定return时，函数返回一个none
'''

def sum2(arg1,arg2):
    return arg1+arg2
sum2(10,20)

'''
python 作用域
L （local）局部作用域
E （Enclosing）闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
Python 以   L -> E -> G -> B 的顺序查找
'''

#作用域演示

x = int(2.9)  # 内建作用域
 
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
#特殊的是，Python中只有 module class def lambda 会引入新的作用域
#而if /else if while 等并不会开辟新作用域，既其内部声明的变量外部也能访问

if True :
    msg = '''我真的
    是一个 全局变量 外部 能访问我！！！'''
print(msg)

'''
global nonlocal
global 可以将指定内部变量是外部的那个重命变量
nonlocal 可以指定内部函数的变量是内部函数外的重命变量
'''

#global
num = 1
def fun1():
    global num #指定是外部的那个num
    print(num)
    num += 100
fun1()
print(num)


#nonlocal
def outer1():
    num = 10
    def inner1():
        nonlocal num #指定了是外面的那个num
        print(num)
        num = 100
    inner1()
    print(num)
outer1()