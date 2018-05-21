'''
set的定义就不用赘述了，各种语言都会声明一遍
使用 {} 或者 set() 创建集合
另外，空集合必须使用set()
因为{}用来创建空字典
'''
student = {'Tom','Jim','Mary','Tom','Jack',"Rose"}

#set 会自动去除重复的元素
print(student)

#测试成员的存在
if('Rose' in student):
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

#使用set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

#这里需要注意 set() 函数接受可迭代对象
#可迭代对象指的是string、list和tuple（也可以自定义可迭代类）
print(a)
print(b)
print(a-b)  #差集
print(a | b)#并集
print(a & b)#交集
print(a ^ b)#不同时存在的元素 a|b - a & b