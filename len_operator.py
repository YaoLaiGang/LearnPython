'''
这篇主要讲解了Python的运算符，由于运算符已经在各种语言上学了N遍
所以就简要的记录下Python的独特之处
'''

#算术运算符中，注意** 和 //
print(9.0//2.0,3**3)

#相应的赋值运算符注意**=和//=
c = 3
a = 2
c **= a
print(c)
c //= a
print(c)

#python的逻辑运算符比较奇特，和其他语言的完全不同
a , b = 10 , 20

if (a and b):
    print('变量 a 和 b 都为 true')
else:
    print('变量 a 和 b 有一个不为true')

a = 0
if a or b:
    print('变量 a 或 b 至少有一个为true')
else:
    print('变量 a , b 均为false')

if not(a and b):
    print('a , b 至少有一个false')
else:
    print('a , b 均为true')

'''
python 拥有比较特殊的成员操作符
in : 在指定序列中找到为true ， 否则为false
not in : 与 in 相反
'''
a , b = 10 , 20
list1 = [1,2,3,4,5]

if a in list1:
    print('变量 a 在list中')
else:
    print('变量 a 不在list中')

if b not in list1:
    print('变量 b 不在list 中')
else:
    print('变量 b 在 list 中')

'''
python 特有的身份运算符
is : 判断两个指针是否引向同一个对象 
is not : 判断两个指针是否引向不同的对象

注：
Python中有 id() 函数，该函数用来获取对象的内存地址
is 类似于 id(x) == id(y)
not is 类似于 id(x) != id(y)
'''
a = b = 20
if a is b:
    print('a b 地址相同')
else:
    print('a b 地址不同')

# 与以下代码等价
a = 10
if id(a)==id(b):
    print('a b 地址相同')
else:
    print('a b 地址不同')

'''
注：is 和 ==的区别
is 判定两个变量是否指向同一个对象 ，类似于java中的 ==
== 判定连个变量的值是否相同，类似于java中的equal
'''