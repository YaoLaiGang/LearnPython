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

print(stack.pop())

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