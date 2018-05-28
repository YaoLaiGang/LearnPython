#…………………………………………………LIST…………………………………………………………………………

'''
List是Python中使用最频繁的数据类型
列表内的数据可以不相同，列表内也可以存放列表
列表写在[]之间，元素用,隔开
与字符串类似，列表也可以被截取
且+为连接运算符，×为重复运算符
'''
list1 = ['abcd',200,3.14,'laigang',20.5]
list2 = [124,'laigang']

print(list1)
print(list1[-1])
print(list1[1:3])
print(list1[2:])
print(list2*2)
print(list1+list2)

#list 中的变量可以改变，Python中只有List和directory内的元素可变
a=[1,2,3,4,5,6]
a[0]=0
a[2:5]=[13,14,15]
print(a)
a[2:5]=[]
print(a)


'''
小结：
1.list写在[]之间，元素用,隔开
2.list可以被索引和切片
3.list使用+拼接
4.list元素可变
'''
 #增加列表元素
list2.append('add')
print(list2)

#删除列表元素

del list2[2]    #直接使用del删除
print(list2)

list2.remove(124)   #使用内置的remove函数删除
print(list2)

#获得长度
print(len(list2))

#判断存在
if 124 in list2:
    pass
else:
    print('list中不存在值124')

#列表的copy
'''
列表的浅copy直接赋值即可，缺点是触一发而动全身
深copy有三种方式
'''
list3 = list2[:]
list3[0] = 'Yao'
print(list3,list2)

import copy
list3 = copy.copy(list2)

list3 = list2.copy()

'''
列表还有一批内置的实用函数，只需查找官方文档即可
'''