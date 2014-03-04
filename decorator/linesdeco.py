__author__ = 'Administrator'
from de03 import logging_decorator
from cashuclass  import print_name

'''
链式。你可以在任意给定的函数中放置多个装饰器。
它使用一种类似用多继承来构造类的方式来构造函数。
'''

@print_name('Sam')
@logging_decorator
def some_function():
    print "I'm the wrapped function!"

some_function()
# >> My name is Sam
# >> The function I modify has been called 1 time(s).
# >> I'm the wrapped function!

"""
当你将装饰器链接在一起时，他们在放置在栈中顺序是从下往上。
被包装的函数，some_fuction，
编译之后，传递给在它之上的第一个装饰器（loging_decorator).
然后第一个装饰器的返回值传递给下一个。
它将以这样的式传递给链中的每一个装饰器。
因为我们这里用到的装饰器都是打印一个值然后返回传递给它们的函数。
这意味着在链中的最后一个装饰器，print_name，
当被包装（装饰）的函数调用时，将打印整个输出的第一行。
"""