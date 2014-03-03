__author__ = 'Administrator'
# In the previous example, we used our decorator function by passing the
# function we wanted to modify to it, and assigning the result to a variable
def identity_decorator(func):
    # Everything here happens when the decorator LOADS and is passed
    # the function as described in step 2 above
    def wrapper():
        # Things here happen each time the final wrapped function gets CALLED
        func()
    return wrapper

def logging_decorator(func):
    def wrapper():
        wrapper.count += 1
        print "The function I modify has been called {0} times(s).".format(
              wrapper.count)
        func()
    wrapper.count = 0
    return wrapper

def some_function():
    print "I'm happiest when decorated."

# Here we will make the assigned variable the same name as the wrapped function
some_function = logging_decorator(some_function)
"""
Decorator语法的简要工作原理:
当Python的解释器看到这个被装饰的方法时，
先编译这个方法(some_function), 
然后先给它赋一个名字 'some_function'.
这个方法(some_function)再被传入装饰方法(decorator function)logging_decorator中
装饰方法(decorator function)logging_decorator返回的新方法替代原来的some_function方法, 
与'some_function'这个名字绑定.
"""

'''
希望这里的注释能起到一定的引导作用. 
只有在装饰器所返回的方法中的指令才会在每次调用的时候被执行. 
在被返回函数外的指令只会被执行一次-- 在第二步 当装饰器第一次接受一个方法的时候。

'''