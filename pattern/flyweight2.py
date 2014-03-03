__author__ = 'Administrator'
class FlyweightFactory(object):
    def __init__(self, cls):
        self._cls = cls
        self._instances = dict()
    # 使用*args, **kargs这样的方式抽象实现的cls的参数数量和类型
    def get_instance(self, *args, **kargs):
        # 如果键在字典中，返回这个键所对应的值。如果键不在字典中，向字典 中插入这个键
        return self._instances.setdefault(
                                (args, tuple(kargs.items())),
                                self._cls(*args, **kargs))


class Spam(object):
    # 我这里实现的是3个参数，这个随意
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Egg(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


SpamFactory = FlyweightFactory(Spam)
EggFactory = FlyweightFactory(Egg)

assert SpamFactory.get_instance(1, 2, 3) is SpamFactory.get_instance(1, 2, 3)
assert EggFactory.get_instance('a', 'b', 'c') is EggFactory.get_instance('a', 'b', 'c')
assert SpamFactory.get_instance(1, 2, 3) is not EggFactory.get_instance(1, 2, 3)