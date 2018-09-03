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


