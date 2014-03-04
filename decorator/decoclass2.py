__author__ = 'Administrator'
"""
装饰器不仅仅可以装饰一个类，它可以作为一个类来使用。
一个装饰器的唯一需求是他的返回值可以被调用。
这意味着当你调用一个对象时它必须实现_call_这个魔幻般的在幕后调用的方法。
函数设置了这个隐式方法。让我们重新建立 identity_decorators 作为一个类，
然后来看它是怎么运作的。
"""
class IdentityDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        self.func()


@IdentityDecorator
def a_function():
    print "I'm a normal function."

a_function()
# >> I'm a normal function