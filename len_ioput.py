from datetime import datetime
#对Python输入输出的基本操作

#输出的美化 (str() 和 repr() 函数 ，两者都可以让变量、常量转化为字符串
#其中 str()函数让用户易懂 repr() 让解释器易懂
#str 函数的本质是对象的 __str__ 方法 ， repr 本质是调用__repr__方法

print(str('hello') , repr('hello'),'hello'.__str__(),'hello'.__repr__())

#repr 会清晰的显示对象的类，在哪个包，而str只显示用户需要看到的内容，当然具体效果要依赖类定义者对内置函数的定义
now = datetime.now()
print(str(now),"----",repr(now))

#repr 不会让转义字符转义
print(r'hello world \n',repr('hello world \n'))

#str.format( ) 函数可以实现格式化的输出 ， 下面打印一个平方 立方表
#法一，传统C风格对齐法
for x in range(1,11):
    print("%2d%6d%6d"%(x,x**2,x**3))

#法二，format 该方法使用{}标示参数，{}内数字表示参数的下标，不包括命名参数（可以指定变量名）,且位置参数必须在关键字参数前,:后侧表示对齐方式
for x in range(1,11):
    print('{0:2d}{1:6d}{tri:6d}'.format(x,x**2,tri=x**3))

#format的用途还有打印一个很长的格式化字符串，通过变量名而非位置的访问更为方便
table = {'Google': 1, 'IBM': 2, 'Taobao': 3}
print('Taobao:{0[Taobao]:1d};Google:{0[Google]:1d};IBM:{0[IBM]:1d}'.format(table))

#用户输入
str2 = input("请输入：")
print('您输入的是：',str2)

'''   ________________文件读写__________________            '''

#打开文件 foo.txt
f = open("foo.txt","rb+")

#读文件,其中read(size)可以指定大小，默认从当前point到文件末尾
fileStr = f.read()
print(fileStr)

#readline() 顾名思义 ，读一行
fileLine = f.readline()
print(fileLine)

#readlines() 读取文档所有行,放入LIST中，参数可以指定字节数
fileLines = f.readlines()
print(fileLines)

#直接迭代文件也能读取，这个特性是其他语言不具有的
for line in f:
    print(line,end="")

#写文件，写入后返回写入的字节数
f.write("人生苦短，我用Python！ \n 对的，Python是程序员的享受")

#如果想写入非字符串的对象，需要转化为字符串
tuples = ("linux is not unix" , 15)
f.write(str(tuples))

#tell() 告知当前所在的位置是第几个字节
'''
seek(offset,from_what) 重定向
from_what 取值：
0 开头 1 当前 2 结尾
from 默认为0
offset 可以取±，+表示向右，-表示向左

需要注意的是，打开文件不使用b模式，只能从文件当前位置定位
'''
f.seek(5)#文件的正数第五个字节
f.read(1)
f.seek(-3,2)#文件的倒数第三个字节
f.read(1)
#关闭文件
f.close()

#使用with读取文件更为方便，并且with已经内置了异常处理,内置了资源释放
#自动调用内置函数 __enter__ __exit__
with open("foo.txt","r+") as f:
    print(f.read())
