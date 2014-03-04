__author__ = 'Administrator'
'''
装饰器是一个可以修饰函数，类或方法的函数。
'''
foo = ['important', 'foo', 'stuff']


def add_foo(klass):
    klass.foo = foo
    return klass


@add_foo
class Person(object):
    pass

brian = Person()

print brian.foo
# >> ['important', 'foo', 'stuff']