__author__ = 'Administrator'
#Python中没有任何手段禁止对用来指代函数式表达式的名字进行重新绑定。
'''
>>> car = lambda lst: lst[0]
>>> cdr = lambda lst: lst[1:]
>>> sum2 = lambda lst: car(lst)+car(cdr(lst))
>>> sum2(range(10))
>>> car = lambda lst: lst[2]
>>> sum2(range(10))
’‘’
‘’‘
functional模块随同Bindings一起还提供了一个叫做namespace的函数，这个函数从Bindings实例中弄出了一个命名空间 (实际就是个字典) 。如果你想计算一个表达式，而该表达式是在定义于一个Bindings中的一个（不可变）命名空间中时，这个函数就可以很方便地拿来使用。Python的eval()函数允许在命名空间中进行求值。举个例子就能说明这一切：
Python中使用不可变命名空间的FP编程片段
>>> let = Bindings()      # "Real world" function names
>>> let.r10 = range(10)
>>> let.car = lambda lst: lst[0]
>>> let.cdr = lambda lst: lst[1:]
>>> eval('car(r10)+car(cdr(r10))', namespace(let))
>>> inv = Bindings()      # "Inverted list" function names
>>> inv.r10 = let.r10
>>> inv.car = lambda lst: lst[-1]
>>> inv.cdr = lambda lst: lst[:-1]
>>> eval('car(r10)+car(cdr(r10))', namespace(inv))
17
 functional模块提供了一个叫做Bindings(由鄙人向Keller进行的提议，proposed to Keller by yours truly)的类，可以用来避免这种重新绑定（至少可以避免意外的重新绑定，Python并不阻止任何拿定主意就是要打破规则的程序员）。尽管要用Bindings类就需要使用一些额外的语法，但这么做就能让这种事故不太容易发生。 Keller在functional模块里给出的例子中，有个Bindings的实例名字叫做let（我推测这么叫是为了仿照ML族语言中的let关键字）。例如，我们可以这么做：
'''
#Python中对重新绑定进行监视后的FP编程片段
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
>>> car(range(10))
0
'''

