__author__ = 'Administrator'
metaflyweight = lambda name, parents, attrs: type(
        name,
        parents,
        dict(attrs.items() + [
            ('__instances', dict()),
            ('__new__', classmethod(
                lambda cls, *args, **kargs: cls.__instances.setdefault(
                                tuple(args),
                                super(type(cls), cls).__new__(*args, **kargs))
                )
            )
        ])
    )


class Spam(object):
    __metaclass__ = metaflyweight

    def __init__(self, a, b):
        self.a = a
        self.b = b


class Egg(object):
    __metaclass__ = metaflyweight

    def __init__(self, x, y):
        self.x = x
        self.y = y


assert Spam(1, 2) is Spam(1, 2)
assert Egg('a', 'b') is Egg('a', 'b')
assert Spam(1, 2) is not Egg(1, 2)

print Spam(1, 2) is Spam(1, 2) ,Egg('a', 'b') is Egg('a', 'b'),Spam(1, 2) is not Egg(1, 2)