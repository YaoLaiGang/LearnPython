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