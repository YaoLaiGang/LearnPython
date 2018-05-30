"""
字典是通过键值对存储的列表，list是通过下标存储的
两者都是可变的
"""
d = {}
d['fname'] = 'first name : LaiGang'
d['lname'] = 'last name : Yao'

d2 = {'name' : 'runoob' , 'code' : 1 , 'site' : 'www.runoob.com'}

print(d['fname'])
print(d['lname'])
print(d2)


#除了上述两种初始化方式外，还有构造函数初始化
d3=dict([('Runoob',1),('Google',2),('Taobao',3)])
print(d3)

d3 = {x : x**2 for x in (2,4,6)}
print(d3)

d3 = dict(Runoob=1,Google=2,Taobao=3)
print(d3)

#字典也有许多内置的函数，可以查阅文档来使用

#增加字典的元素
d2['id'] = 1
print(d2)

#删除字典的元素
print(d2.pop('id')) #删除并返回其value
print(d2.popitem()) #随机删除并返回整个键值对
'''
小结：
字典是一种映射类型，存储的东西是键值对
字典的关键字不可变，但是value可变
创建空字典用{}，创建空Set用set()
'''