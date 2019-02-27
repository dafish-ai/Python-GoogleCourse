'''
类学习作业讲解
'''

"""
作业一：
定义一个父类people,包含姓名，年龄，eat()方法。
定义两个子类，Chinese和American，均含有eat()方法。
实例化子类对象，并实现调用父类的eat()方法。
"""
"""
解析：
本题围绕类这个知识点展开，涉及类的定义、类变量设置、类方法设置
类的继承、类的实例化以及参数方法调用
一般类的定义用关键字"class"，成员变量放在初始化函数中（可以自定义初始化）
类方法和普通函数一样，参数列表多了一个self,表示类本身，可以在方法里调用类方法或者类变量
类的继承比较简单，直接在类名后的括号内写父类名称即可，默认是Object
"""



# 父类
class people():
    # 初始化函数
    def __init__(self, name, age):
        self.name = name    # 姓名
        self.age = age     # 年龄

    # 定义一个类方法eat
    def eat(self):
        print("%s在吃白饭"%self.name)


# American继承自people
class American(people):
    # 自己实现eat()方法
    def eat(self):
        print("%s在吃American饭"%self.name)


class Chinese(people):
    # 自己实现eat()方法
    def eat(self):
        print("%s在吃Chinese饭"%self.name)


p = people("张三", 20)  # 实例化对象
p.eat()   # 调用eat方法
chinese = Chinese("李四", 15)   # 实例化对象
chinese.eat()  # 调用eat方法
american = American("王五", 18)    # 实例化对象
american.eat()   # 调用eat方法

"""
运行结果：
张三在吃白饭
李四在吃Chinese饭
王五在吃American饭
"""
