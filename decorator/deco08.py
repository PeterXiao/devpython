__author__ = 'Administrator'
def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()

	
'''
装饰器的核心作用是name binding。
这种语法是Python多编程范式的又一个体现。
大部分Python用户都不怎么需要定义装饰器，
但有可能会使用装饰器。鉴于装饰器在Python项目中的广泛使用，
了解这一语法是非常有益的。
'''