#Python的面向对象OO，老生常谈的东西，封装、继承、多态
'''
类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，
方法中可以调用基类中的同名方法。
'''

#类定义
class Dog:
    """小狗类"""
    weight = 0 #体重
    name = ''
    __gender = ''

    #类方法必须包含self，并且是第一个参数，以__开头的方法是私有方法，只能在类内部访问

    #private
    def __sleep(self):
        print('睡好才有精神')

    def getGender(self):
        return self.__gender

    #public
    def bark(self):#self 是对象自己
        self.__sleep()  #内部访问需要self（自指针）指定
        print('汪汪汪')


    #构造方法
    def __init__(self,weight = 20 , name = '旺财' , gender = 'man'):#默认参数
        self.weight = weight
        self.name = name
        self.__gender = gender

#实例化
dogWang = Dog(50,'团团','women')

#方法和属性的访问
print('我是',dogWang.name,'我的重量是',dogWang.weight,'我的性别是',dogWang.getGender())
dogWang.bark()

#上面的访问控制符体现了Python面向对象对封装的实现，下面是继承
#Python支持多继承

'''
class DerivedClass(BaseClass1, BaseClass2,..., BaseClassN):
    类的属性
    类的方法

注意基类的排列顺序，当子类调用自身没有定义的方法，
也并没有指定具体的基类名称时，
python会从左到右依次查找继承的基类中是否包含该方法，直到找到就停止，
否则报错。

基类定义可以在其他模块，比如：
class DerivedClassName(modname.BaseClassName):
'''
#单继承
class ColorDog(Dog):
    color = 'black'

    #覆盖父类方法
    def bark(self):
        print('汪汪汪 from black dog')
 
    
    def __init__(self , weight = 20 , name = '旺财' , gender = 'man',color = 'black'):
        Dog.__init__(self,weight,name,gender) #调用父类方法,别忘了self
        self.color = color

dogBlack = ColorDog(weight=50,color='blue')

print('我是',dogBlack.name,'我的重量是',dogBlack.weight,'我的性别是',dogBlack.getGender(),'我的颜色是',dogBlack.color)
dogBlack.bark()
super(ColorDog,dogBlack).bark()


#运算符重载，具有和C++类似的功能
class Integer:
    num = 0
    def __init__(self,num):
        self.num = num
    
    def __add__(self,other):
        return Integer(self.num+other.num)

    def __str__(self):
        return str(self.num)

a , b = Integer(1) , Integer(1)
print(a+b)
