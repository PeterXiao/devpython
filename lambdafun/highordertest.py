__author__ = 'Administrator'
#Python内建的三个最常用的高阶函数是：map()、reduce()和filter()。这三个函数所做的事情 —— 以及谓之为“高阶”（higher-order）的原因 —— 是接受其它函数作为它们的（部分）参数。还有别的一些不属于内置的高阶函数，还会返回函数对象。
def foo_factory():
  def foo():
        print（"Foo function from factory"）

  return foo
        ...
#f = foo_factory()
#f() # Foo function from factory
'''
  可能其中最著名、最有用和最重要的高阶函数要数curry()了。
  函数curry()的名字取自于逻辑学家Haskell Curry，
  前文提及的一种编程语言也是用他姓名当中的名字部分命名的。"currying"背后隐含的意思是，
  （几乎）每一个函数都可以视为只带一个参数的部分函数（partial function）。
  要使currying能够用起来所需要做的就是让函数本身的返回值也是个函数，
  只不过所返回的函数“缩小了范围”或者是“更加接近完整的函数”。
  这和我在第二部分中提到的闭包特别相似 ——
  对经过curry后的返回的后继函数进行调用时一步一步“填入”最后计算所需的更多数据
  （附加到一个过程（procedure）之上的数据）

  Haskell
  computation a b c d = (a + b^2+ c^3 + d^4)
check = 1 + 2^2 + 3^3 + 5^4

fillOne   = computation 1
-- specify "a"
fillTwo   = fillOne 2
-- specify "b"
fillThree = fillTwo 3
-- specify "c"
answer    = fillThree 5
-- specify "d"


-- Result: check == answer == 657

在Python计算中使用Curry
>>> from functional import curry
>>> computation = lambda a,b,c,d: (a + b**2 + c**3 + d**4)
>>> computation(1,2,3,5)
657
>>> fillZero  = curry(computation)
>>> fillOne   = fillZero(1)
# specify "a"
>>> fillTwo   = fillOne(2)
# specify "b"
>>> fillThree = fillTwo(3)
# specify "c"
>>> answer    = fillThree(5)
# specify "d"
>>> answer
657
  '''

"""
Python中curry后的计税程序
from functional import *

taxcalc = lambda income,rate,deduct: (income-(deduct))*rate

taxCurry = curry(taxcalc)
taxCurry = taxCurry(50000)
taxCurry = taxCurry(0.30)
taxCurry = taxCurry(10000)
print "Curried taxes due =",taxCurry

print "Curried expression taxes due =", \
      curry(taxcalc)(50000)(0.30)(10000)
  """

#和使用闭包不同，我们需要以特定的顺序（从左到右）对参数进行curry处理。当要注意的是，functional模块中还包含一个rcurry()类，能够以相反的方向进行curry处理（从右到左）。
#从一个层面讲，其中的第二个print语句同简单的同普通的taxcalc(50000,0.30,10000)函数调用相比只是个微小的拼写方面的变化。但从另一个不同的层面讲，它清晰地一个概念，
# 那就是，每个函数都可以变换成仅仅带有一个参数的函数，这对于刚刚接触这个概念的人来讲，会有一种特别惊奇的感觉。
'''
  它里面的其它高阶函数在很大程度上感觉有点象是“增强”版本的标准高阶函数map()、filter()和reduce()。
  这些函数的工作模式通常大致如此：将一个或多个函数以及一些列表作为参数接收进来，
  然后对这些列表参数运行它前面所接收到的函数。在这种工作模式方面，
  有非常大量很有意思也很有用的摆弄方法。还有一种模式是：拿到一组函数后，
  将这组函数的功能组合起来创建一个新函数。这种模式同样也有大量的变化形式。
  下面让我们看看functional模块里到底还有哪些其它的高阶函数。
sequential()和also()这两个函数都是在一系列成分函数（component function）的基础上
创建一个新函数。然后这些成分函数可以通过使用相同的参数进行调用。
两者的主要区别就在于，sequential()需要一个单个的函数列表作为参数，
而also()接受的是一系列的多个参数。在多数情况下，对于函数的副作用而已这些会很有用，
只是sequential()可以让你随意选择将哪个函数的返回值作为组合起来后的新函数的返回值。
  '''
"""
>>> def a(x):
...     print x,
...     return "a"
...
>>> def b(x):
...     print x*2,
...     return "b"
...
>>> def c(x):
...     print x*3,
...     return "c"
...
>>> r = also(a,b,c)
>>> r
<functional.sequential instance at 0xb86ac>
>>> r(5)
5 10 15
'a'
>>> sequential([a,b,c],main=c)('x')
x xx xxx
'c'

 """
'''
而any()、all()和 none_of()这三个让你可以使用一个参数列表对同一个函数进行多次调用。
在大的结构方面，这些函数同内置的map()、reduce()和filter()有点象。
但funtional模块中的这三个高阶函数中都是对一组返回值进行布尔（boolean）运算得到其返回值的。
对一系列返回值的真、假情况进行判断
>>> from functional import *
>>> isEven = lambda n: (n%2 == 0)
>>> any([1,3,5,8], isEven)
1
>>> any([1,3,5,7], isEven)
0
>>> none_of([1,3,5,7], isEven)
1
>>> all([2,4,6,8], isEven)
1
>>> all([2,4,6,7], isEven)
0
'''
#有点数学基础的人会对这个高阶函数非常感兴趣：iscompose().
#  将多个函数进行合成（compostion）指的是，将一个函数的返回值同下个函数的输入“链接到一起”。
# 对多个函数进行合成的程序员需要负责保证函数间的输入和输出是相互匹配的，
# 不过这个条件无论是程序员在何时想使用返回值时都是需要满足的。举个简单的例子和阐明这一点：
  #创建合成函数
  '''
  >>> def minus7(n): return n-7
...
>>> def times3(n): return n*3
...
>>> minus7(10)
3
>>> minustimes = compose(times3,minus7)
>>> minustimes(10)
9
>>> times3(minus7(10))
9
>>> timesminus = compose(minus7,times3)
>>> timesminus(10)
23
>>> minus7(times3(10))
23

  '''
