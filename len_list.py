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
 