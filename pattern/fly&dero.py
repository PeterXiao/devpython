__author__ = 'Administrator'
# 这个是装饰器，主要用来将操作工厂当参数传入，拦截操作工厂的调用
class flyweight(object):
    def __init__(self, cls):
        self._cls = cls
        self._instances = dict()
    # 重载括号操作符， 你想啊，加了装饰器就会调用，也就会触发__call__
    def __call__(self, *args, **kargs):
        return self._instances.setdefault(
                                    (args, tuple(kargs.items())),
                                    self._cls(*args, **kargs))


@flyweight
class Spam(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


@flyweight
class Egg(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


assert Spam(1, 2) is Spam(1, 2)
assert Egg('a', 'b') is Egg('a', 'b')
assert Spam(1, 2) is not Egg(1, 2)
print Spam(1, 2) is Spam(1, 2) ,Egg('a', 'b') is Egg('a', 'b'),Spam(1, 2) is not Egg(1, 2)