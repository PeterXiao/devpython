__author__ = 'Administrator'
class circle(object):
    def __init__(self,radius):
        self.radius =radius
c = circle(4.0)
d = circle(5.0)
class C1(object):
    x =23
print(C1.x)
class c2(object):pass
c2.x =23
print(c2.x)
print( C1.__name__,C1.__bases__)
#对于包含在类体中的语句使用该类的属性，必须是永恒属性的简单名称
#但是在类体中定义的方法的语句中，引用类的属性，必须使用完整名称。这是因为作用域的问题
