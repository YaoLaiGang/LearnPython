'''
我们先熟悉下List，然后再用它来模拟常见的数据结构
'''
#常用方法
a = [2333,333,333,333,123,2.3]

print(a.count(333))

a.insert(2,666)
a.append(777)
print(a)

a.index(333)

a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

#对于修改列表的方法，没有返回值

'''
使用列表的 append pop 来模拟栈
'''
stack = [3,4,5]
stack.append(6) #压栈
stack.append(7)
print(stack)

print(stack.pop())#出栈

'''
使用deque来模拟队列
'''
from collections import deque
queue = deque(['jobs','gall','jack'])
queue.append('terry') #入队
queue.popleft() #出队

'''
列表推导式
将一些操作应用于某个序列的每个元素，并将获得的元素作为新的列表的元素
或者对某个序列的元素进行判定，来生成新的序列

推导式的语法
1.每个列表推导式都在for以后跟一个表达式，并拥有0到多个for 或者 if子句
2.如果想要结果是元组，可以使用括号
'''
#将list中所有元素*3生成新的元素
vec = [1,3,5]
print([3*x for x in vec])

#生成x 和它的开方
print([[x,x**2] for x in vec])

#对所有元素调用strip方法
fruit = ['    banana',' loganberry',' watermelon ']
print([x.strip() for x in fruit])

#for 后 跟 if 进行过滤处理
#大于三的元素*3返回
print([3*x for x in vec if x > 3])

#for 后跟for 实现对两个元组的交叉操作
#笛卡尔积
vec1 = [2,4,6]
vec2 = [1,3,5]

print([x*y for x in vec1 for y in vec2])

#对应项相乘
print([vec1[i]*vec2[i] for i in range(len(vec1))])

#如果前面的能搞明白，那么下面这个也应该绰绰有余
print([str(round(355/113,i)) for i in range(1,6)])

#矩阵的模拟,使用嵌套LIST
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

#将3*4矩阵转化为4*3矩阵（矩阵转置）
print([[ matrix[0][i] , matrix[1][i] , matrix[2][i]] for i in range(4) ])

print([[row[i] for row in matrix] for i in range(4)])#外侧有一个值，内侧再循环一遍

#使用循环来解决这个问题
transposed = []
for i in range(4):  #第几列
    row = []
    for j in range(3):  #第几行
        row.append(matrix[j][i])
    transposed.append(row)
print(transposed)

#解法二
transposed.clear
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

'''
del 对LIST的切割
del的删除和LIST的删除不一样，del的删除可以使用访问列表时的步进删除
'''
a = [1,2,3,4,5,6,7,8]
del a[0]
a
del a[2:4]
a
del a[:]
a

'''
元组的基本使用
'''
t = 123,345,456 #声明可以不带括号,如果元组是更大的一部分就需要
print(t)

#嵌套
u = t , (1,2,3,4,5)
print(u)

#推导式生成set集合
a = {x for x in 'afefadfefjaofnwe' if x not in 'abc'}

#字典的遍历技巧，在遍历字典时，可以使用items方法同时获得键值
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

#list中遍历时，可以使用enumerate()获得其下标
for i,v in enumerate(['baidu','ali','tencent']):
    print(i,v)

#遍历多个序列，使用zip()函数,该函数是一一对应的，不是笛卡尔积
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print("what is your %s It is %s"%(q,a))

#反向遍历序列，使用reversed()函数，或者使用倒着的步进

#reversed()函数
for q in reversed(questions):
    print(q)

#逆向步进
for i in range(len(questions)-1,-1,-1):
    print(questions[i])

#有序遍历序列 ， sorted()函数
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(basket):
    print(fruit)