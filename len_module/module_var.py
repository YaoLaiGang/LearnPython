foo = 0 #模块中的变量

def show() :
    print(foo)

if __name__ == "_main_" : #判断是否以主程序的形式运行
    show()

'''
python 查找包的顺序如下：
首先，Python 会在内建模块中搜寻 foobar；
若未找到，则 Python 会在当前工作路径（当前脚本所在路径，或者执行 Python 解释器的路径）中搜寻 foobar；
若仍未找到，则 Python 会在环境变量 PYTHONPATH 中指示的路径中搜寻 foobar；
若依旧未能找到，则 Python 会在安装时指定的路径中搜寻 foobar；
若仍旧失败，则 Python 会报错，提示找不到 foobar 这个模块。
'''

'''
python中把多级含有module的文件夹称为包 
许多重要的Python的Module都是以包的形式发布的
需要注意的是每一级目录下都要有__init__.py，用来表示这是一个包
当然len_moudle下面也不例外
'''