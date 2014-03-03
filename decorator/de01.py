__author__ = 'Administrator'
#Decorator是一个改变其他方法的方法.
#我们可以以类似其它对象的方式传递对象。
# 它可以是字典的值、列表的项或是另一个对象的属性。
# 那么，我们不能将函数以参数的方式传递给另一个函数么？
# 可以！函数作为参数传递给高阶函数。

def traveling_function():
    print "Here I am!"

function_dict = {
    "func": traveling_function
}

def self_absorbed_function():
    return "I'm an amazing function!"

def printer(func):
    print "The function passed to me says: " + func()

# Call `printer` and give it `self_absorbed_function` as an argument


trav_func = function_dict['func']
trav_func()

# Call `printer` and give it `self_absorbed_function` as an argument
printer(self_absorbed_function)