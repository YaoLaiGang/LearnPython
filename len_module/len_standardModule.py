import sys

print('命令行参数如下：')
for i in sys.argv: #这是一个包含命令行参数的列表
    print(i)

print('python 路径为',sys.path)#path包含了Python解释器自动查找模块位置的列表