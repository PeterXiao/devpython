__author__ = 'Administrator'
class Spam(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class SpamFactory(object):
    def  __init__(self):
        self.__instances = dict()

    def get_instance(self, a, b):
        # 在实例化后生成一个字典，当新的元祖对不存在就缓存起来
        if (a, b) not in self.__instances:
            self.__instances[(a, b)] = Spam(a, b)
        return self.__instances[(a, b)]

# 这个和上面的意思完全一样， 这是为了在最后断言下2个工厂缓存的数据是不是能共享
class Egg(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class EggFactory(object):
    def __init__(self):
        self.__instances = dict()

    def get_instance(self, x, y):
        if (x, y) not in self.__instances:
            self.__instances[(x, y)] = Egg(x, y)
        return self.__instances[(x, y)]

spamFactory = SpamFactory()
eggFactory = EggFactory()

assert spamFactory.get_instance(1, 2) is spamFactory.get_instance(1, 2)
assert eggFactory.get_instance('a', 'b') is eggFactory.get_instance('a', 'b')
# spamFactory存储的这个元祖和eggFactory存储的不是一个东西
assert spamFactory.get_instance(1, 2) is not eggFactory.get_instance(1, 2)



