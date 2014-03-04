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

# In the previous example, we used our decorator function by passing the
# function we wanted to modify to it, and assigning the result to a variable

def some_function():
    print "I'm happiest when decorated."

# Here we will make the assigned variable the same name as the wrapped function
some_function = logging_decorator(some_function)

# We can achieve the exact same thing with this syntax:

@logging_decorator
def some_function():
    print "I'm happiest when decorated."

# （译注：形式参数示例）
def function_with_many_arguments(*args):
    print args

# 此函数中的`args`将成为传递的所有参数的元组
# 可以在函数中像使用元组一样使用
function_with_many_arguments('hello', 123, True)
# >> ('hello', 123, True)

# （译注：实参示例）
def function_with_3_parameters(num, boolean, string):
    print "num is " + str(num)
    print "boolean is " + str(boolean)
    print "string is " + string

arg_list = [1, False, 'decorators']

# 通过使用'*'号 arg_list将会被展开为三个位置参数
function_with_3_parameters(*arg_list)
# >> num is 1
# >> boolean is False
# >> string is decorators
'''
重申：在形式参数列表中，*arg将放到一个名为args的元组中，
在一个实参列表中，*arg将扩展成一系统位置参数然后应用到函数中。
正如你在实参示例所看到那样，'*'符号可以和'args'之外的的名字使用。
它只是一个在收缩和扩展通用列表时的约定形式。
**kwargs跟他的兄弟*args相似，但是它是跟关键词参数相关而不是位置。
如果**kwargs用在一个形式参数列表中，它将所有接收到的关键词参数收集进一个字典中。
如果它用在一个函数的实参列表中。它将把一个字典扩展成一系统的关键词参数

'''

def function_with_many_keyword_args(**kwargs):
     print kwargs

function_with_many_keyword_args(a='apples', b='bananas', c='cantalopes')
# >> {'a': 'apples', 'b': 'bananas', 'c': 'cantalopes'}  def multiply_name(count=0, name=''):
#print (name * count)

arg_dict = {'count': 3, 'name': 'Brian'}

#multiply_name(**arg_dict)
# >> BrianBrianBrian
