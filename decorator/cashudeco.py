__author__ = 'Administrator'
"""

有时你需要根据不同的情况改变装饰器的行为，这可以通过传递参数来完成。
"""

from functools import wraps


def argumentative_decorator(gift):
    def func_wrapper(func):
        @wraps(func)
        def returned_wrapper(*args, **kwargs):
            print "I don't like this " + gift + " you gave me!"
            return func(gift, *args, **kwargs)
        return returned_wrapper
    return func_wrapper


@argumentative_decorator("sweater")
def grateful_function(gift):
    print "I love the " + gift + "! Thank you!"

grateful_function()
# >> I don't like this sweater you gave me!
# >> I love the sweater! Thank you!

# If we tried to invoke without an argument:
#grateful_function = argumentative_function(grateful_function)

# But when given an argument, the pattern changes to:
grateful_function = argumentative_decorator("sweater")(grateful_function)
'''
主要的要关注的是当给定一些参数，
装饰器会首先被引用并带有这些参数——就像平时包装过的函数并不在此列。
 然后这个函数调用返回值， 装饰器已经包装的这个函数已经传递给初始化后的带参数的装饰器的返回函数。
 （这种情况下， 返回值是(argumentative_decorator("swearter")).
1. 解释器到达装饰过的函数, 编译grateful_function, 并把它绑定给'grateful_fucntion'这个名字.
2. argumentativ_decorator被调用, 并传递参数“sweater”, 返回func_wrapper.
3. func_wrapper被调用, 并传入grateful_function作为参数, func_wrapper返回returned_wrapper.
4. 最后， returned wrapper 被替代为原始的函数 grateful_function, 然后被绑定到grateful function这个名字下.
'''