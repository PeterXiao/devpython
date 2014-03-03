__author__ = 'Administrator'
"""从心而论，decorator 只是将函数作为参数的函数。
通常，它的作用是返回封装好的经过修饰的函数。
下面这个简单的身份识别 decorator
 可以让我们了解 decorator 是如何工作的。"""
def identity_decorator(func):
    def wrapper():
        func()
    return wrapper


def a_function():
    print "I'm a normal function."

# `decorated_function` is the function that `identity_decorator` returns, which
# is the nested function, `wrapper`
decorated_function = identity_decorator(a_function)

# This calls the function that `identity_decorator` returned
decorated_function()
# >> I'm a normal function

"""
在这里，identity_decoratordoes 并没有修改其封装的函数。
它仅仅是返回了这个函数，
调用了作为参数传递给 identity_decorator 的函数。
这个 decorator 毫无意义！
有趣的是在 identity_decorator 中，
虽然函数没有传递给 wrapper ，
它依然那可以被调用，这是因为闭包原理。
"""


"""
闭包

闭包是个花哨的术语，意思是当一个函数被声明，
在其被声明的词法环境中，它都可以被引用。
上例中，当 wrapper 被定义时，
它就访问了本地环境中的函数变量。
一旦 identity_decorator 返回，
你就只能通过 decorated_function 访问函数。
在 decorated_function 的闭包环境之外，
函数并非以变量形式存在的。

"""