__author__ = 'Administrator'
"""
代码记忆是一种避免潜在的重复计算开销的方法。
你通过缓存一个函数每次运行的结果来达到此目的。
这样，下一次函数以同样的参数运行时，
它将从缓存中返回结果，并不需要花费额外的时间来计算结果。
"""

from functools import wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def an_expensive_function(arg1, arg2, arg3):
    print(arg1,arg2,arg3)


an_expensive_function(123,234,456)


"""
使用装饰器的一个副作用就是，
装饰之后函数丢失了它本来的__name__,__doc__及__module__属性。
包装函数用作装饰器来包装装饰器返回的函数，如果被包装的函数没有被装饰，
则将恢复他们所有的三个属性值。 例如：
一个_expensive_function的名字（可以通过_expensive_function.__name__来查看）将被包装，
即使我们没有使用装饰器。

"""