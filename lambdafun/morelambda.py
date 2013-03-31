__author__ = 'Administrator'
#表达式绑定
#具有重新绑定向导的 Python 函数式编程(FP)
'''
>>> from functional import *
>>> let = Bindings()
>>> let.car = lambda lst: lst[0]
>>> let.car = lambda lst: lst[2]
Traceback (innermost last):
  File "<stdin>", line 1, in ?
  File "d:\tools\functional.py", line 976, in __setattr__

raise BindingError, "Binding '%s' cannot be modified." % name
functional.BindingError:  Binding 'car' cannot be modified.
>>> let.car(range(10))
0
'''

"""
绑定类在一个模块或者一个功能定义范围内做这些我们希望的事情，但是没有办法在一条表达式内使之工作。然而在ML家族语言(译者注：ML是一种通用的函数式编程语言),在一条表达式内创建绑定是很自然的事。
-- car (x:xs) = x  -- *could* create module-level binding
list_of_list = [[1,2,3],[4,5,6],[7,8,9]]

-- 'where' clause for expression-level binding
firsts1 = [car x | x <- list_of_list] where car (x:xs) = x

-- 'let' clause for expression-level binding
firsts2 = let car (x:xs) = x in [car x | x <- list_of_list]

-- more idiomatic higher-order 'map' technique
firsts3 = map car list_of_list where car (x:xs) = x

-- Result: firsts1 == firsts2 == firsts3 == [1,4,7]
"""

'''
Greg Ewing 发现用Python的list概念实现同样的效果是有可能的；甚至我们可以用几乎与Haskell语法一样干净的方式做到。
Python 2.0+ 命名绑定表达式
>>> list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
>>> [car_x for x in list_of_list for car_x in (x[0],)]
[1, 4, 7]
'''


#Python中的使用块级绑定的'map()'
'''
>>> list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
>>> let = Bindings()
>>> let.car = lambda l: l[0]
>>> map(let.car,list_of_list)
[1, 4, 7]
'''

#这样真不错，但如果我们想使用函数map()，那么其中的绑定范围可能会比我们想要的更宽一些。然而，我们可以做到的，哄骗列表解析让它替我们做名字绑定，即使其中的列表并不是我们最终想要得到的列表的情况下也没问题：
#从Python的列表解析中“走下舞台”

# Compare Haskell expression:
# result = func car_car
#          where
#              car (x:xs) = x
#              car_car = car (car list_of_list)
#              func x = x + x^2
#  [func for x in list_of_list for car in (x[0],)for func in (car+car**2,)][0]
#我们对list_of_list列表中第一个元素的第一个元素进行了一次算数运算，而且期间还对该算术运算进行了命名（但其作用域仅仅是在表达式的范围内）。作为一种“优化”，我们可以不用费心创建多于一个元素的列表就能开始运算了，因为我们结尾处用的索引为0，所以我们仅仅选择的是第一个元素。
#列表解析中高效
#>>> [func for x in list_of_list[:1]
#...       for car in (x[0],)
#     ...       for func in (car+car**2,)][0]
#  2
