#本篇探讨Python的基础语法
#默认情况下Python3使用utf-8编码，所以不需要特殊注释就可以使用中文
#让我们开启Python之旅吧
print("hello python")

#输入所有的Python关键字
import keyword
print(keyword.kwlist)

"""
python 的多行注释就是三个引号，且Python不区分单引号和双引号

"""

#注意Python的缩进，这是一个令新手十分头疼的问题
if True:
	print("true")
else:
	print("false")

#如果Python很长，可以使用\来换行
total = "苟利国家生死以" + \
		"岂因祸福" + \
		"趋避之"
print(total)

#python的数字类型共有四种
#python 同一行可以写入多行语句，但要用;分开
a =1 ;t = True ;f = 3.14 ; c= 1+2j
print(c)

#和数字类型对应的是字符串类型
"""
python 中的单引号和双引号完全相同
使用三引号可以指定一个多行字符串
使用转义符 \
使用 r 来输出 \
使用 + 连接，使用 * 重复
两种访问方式，左头为0 ，右头为-1
字符串是不可变得，不要试图改变字符串
Python没有字符，即使是单个的字符也是字符串
字符截取格式 变量[头下标:尾下标]
"""
param = """我是换行的字符串
可以有多行的组成"""
print(param)
print(param[0:-1]) #第一个到最后一个
print(param[0])
print(param[2:5])
print(param[2:])
print(param*2)
print(param+"苟全性命于乱世")
print("**********************************")
print("hello\nworld")
print(r"hello\nworld")

#虽然空行不是语法要求的的，但是空行也是代码的一部分，它的作用是表示一段新的代码的开始

#用户输入
x = input("\n 按下 enter 结束")
print("用户的输入是： " + x)

#同一行运行多条语句,该方法会返回相应的字符个数
import sys ; x='laigang' ; sys.stdout.write(x+'\n')

#print默认换行，不换行需要特殊处理
print("姚来刚",end=" ")

'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''

#导入整个模块
import sys
print("命令行参数为")
for i in sys.argv:
	print(i)
print("\n Python的路径为",sys.path)

#导入sys中的成员
from sys import argv,path
print("path",path)

