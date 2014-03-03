__author__ = 'Administrator'
def logging_decorator(func):
    def wrapper():
        wrapper.count += 1
        print "The function I modify has been called {0} times(s).".format(
              wrapper.count)
        func()
    wrapper.count = 0
    return wrapper


def a_function():
    print "I'm a normal function."

modified_function = logging_decorator(a_function)

modified_function()
# >> The function I modify has been called 1 time(s).
# >> I'm a normal function.

modified_function()
# >> The function I modify has been called 2 time(s).
# >> I'm a normal function.
"""
我们说过一个Decorator会修改另外一个方法, 
这个例子可能会帮助你理解这其中的意思. 
正如你在这个例子中所看到的一样, 
logging_decorator 所返回的新方法和a_function很相似，
只是多增加了日志功能。
在这个例子中，logging_decorator接收一个方法作为参数, 
返回另一个包装过的方法. 每当logging_decorator返回的方法被调用的时候, 
他会为wrapper.count加1, 打印wrapper.count的值, 
然后再调用logging_decorator所包装的方法.
"""