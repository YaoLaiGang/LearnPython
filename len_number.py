#本篇探讨Python的基本类型

#Python的变量就是变量，没有实际类型，赋予什么值就是什么类型
counter = 300       #整型
miles = 1000.0      #浮点型
name = "laigang"    #字符串

print(counter)
print(miles)
print(name)

#和c一样，Python允许连续赋值
a = b = c = 1

#python也运行分别赋值,十分灵活
a , b , c = 1 , 2 ,"python"
print(a,b,c)

"""
Python3 支持六种基本数据类型
Number
String
List
Tuple
Sets
Dictionary
其中，Number String Tuple Sets 是不可变数据
List Dictionary 是可变数据
"""

"""

……………………………………………………Number……………………………………………………………………………………

"""

#Python3中共有 int float bool complex 四种类型
#其中int默认就是长整型
#使用type() 可以查询变量的数据类型

a , b , c , d = 20 , 5.5 , True , 4+3j
print(type(a),type(b),type(c),type(d))

#也可以使用isinstance来判断数据的类型
a=100
print(isinstance(a,int))

#那么instance和type的区别在哪里呢？下面举一个栗子
class A:
    pass
class B(A):
    pass

isinstance(A(),A)   #true
type(A())==A        #true
isinstance(B(),A)   #true
type(B())==A        #false

#区别在于，type不认为子类是一种父类，更为严格
#而isinstance() 是承认子类是父类的一种的

'''
注意，Python中的True和False是两个关键字，但是他们的值还是0,1，并且可以
和数字相加
'''
#当指定一个值的时候，Number对象就会创建
var1 = 1
var2 = 35

#可以使用del关键字来删除一个或多个对象的引用

del var1 , var2

"""
小结
1.Python可同时为多个变量赋值
2.一个变量可以通过赋值指向不同的变量
3.两种除法 / 返回浮点数 // 返回整数
4.混合计算时Python会把整型转化为浮点数
"""