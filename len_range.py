#range()函数是最常用的函数，特别运行测试一下
#一般用法
for i in range(5):
    print(i)
#指定区间
for i in range(5,9):
    print(i)
#指定步长，逆序输出
for i in range(10,0,-1):
    print(i)
for i in range(0,10,3):
    print(i)

#常和len函数搭配使用
a = ['Alibaba','Baidu','HUAWEI','Tencent','Lenovo']
for i in range(len(a)):
    print(i,a[i])

#也可以使用enumerate函数实现上述功能
for i , j in enumerate(a):
    print(i,j)

#亦可使用LIST函数来创建列表
list(range(5))