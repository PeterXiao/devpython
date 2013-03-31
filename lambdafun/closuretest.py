__author__ = 'Administrator'
#闭包（Closure）
#闭包就象是FP的Jekyll，OOP（面向对象编程）的 Hyde （或者可能是将这两个角色互换）（译者注：Jekyll和Hyde是一部小说中的两个人物）. 和象对象实例类似，闭包是一种把一堆数据和一些功能打包一起进行传递的手段。
'''使用冻结变量的Python代码片段

>>> N = 10
>>> def addN(i, n=N):
...     return i+n
...
>>> addN(5)   # Add 10
15
>>> N = 20
>>> addN(6)   # Add 10 (current N doesn't matter)
16
我们冻结的变量实质上就是个闭包。我们将一些数据“附加”到了addN()函数之上。对于一个完整的闭包而言，在函数addN()定义时所出现的数据，应该在该函数被调用时也可以拿到。然而，本例中（以及更多更健壮的例子中），使用缺省参数让足够的数据可用非常简单。函数addN()不再使用的变量因而对计算结构捕获产生丝毫影响。

'''
#先收集一些数据，数据不一定有什么特别的顺序，最后使用所有这些数据进行一个计算。让我们为这种情况些个简化版本的程序：
#Python风格的计税类/实例
class TaxCalc:
    def taxdue(self):return (self.income-self.deduct)*self.rate
taxclass = TaxCalc()
taxclass.income = 50000
taxclass.rate = 0.30
taxclass.deduct = 10000
print"Pythonic OOP taxes due =", taxclass.taxdue()

'''
在我们的TaxCalc类 (或者更准确的讲，在它的实例中)，我们先收集了一些数据，数据的顺序随心所欲，然后所有需要的数据收集完成后，我们可以调用这个对象的一个方法，对这堆数据进行计算。所有的一切都呆在一个实例中，而且，不同的实例可以拥有一堆不同的数据。能够创建多个实例，而多个实例仅仅是数据不同，这通过“全局变量”和“冻结变量”这两种方法是无法办到的。"货船"方法能够做到这一点，但从那个展开的例子中我们能够看出，它可能不得不在开始时就传递多个数值

'''
#Smalltalk风格的(Python) 计税程序

class TaxCalc:
    def taxdue(self):return (self.income-self.deduct)*self.rate
    def setIncome(self,income):
        self.income = income
        return self
    def setDeduct(self,deduct):
        self.deduct = deduct
        return self
    def setRate(self,rate):
        self.rate = rate
        return self
print"Smalltalk-style taxes due =", \
     TaxCalc().setIncome(50000).setRate(0.30).setDeduct(10000).taxdue( )

#通过使用Xoltar toolkit，我们可以生成完整的闭包，能够将数据和函数结合起来，获得我们所需的特性；另外还可以让多个闭包（以前成为对象）包含不同的数据：
#Python的函数式风格的计税程序
from functional import *

taxdue        = lambda: (income-deduct)*rate
incomeClosure = lambda income,taxdue: closure(taxdue)
deductClosure = lambda deduct,taxdue: closure(taxdue)
rateClosure   = lambda rate,taxdue: closure(taxdue)

taxFP = taxdue
taxFP = incomeClosure(50000,taxFP)
taxFP = rateClosure(0.30,taxFP)
taxFP = deductClosure(10000,taxFP)
print"Functional taxes due =",taxFP()

print"Lisp-style taxes due =", \
     incomeClosure(50000,
                   rateClosure(0.30,
                               deductClosure(10000, taxdue)))()

'''
我们所定义的每个闭包函数可以获取函数定义范围内的任意值，然后将这些值绑定到改函数对象的全局范围之中。然而，一个函数的全局范围并不一定就是真正的模块全局范围，也和不同的闭包的“全局”范围不相同。闭包就是“将数据带”在了身边。
在我们的例子中，我们利用了一些特殊的函数把特定的绑定限定到了一个闭包作用范围之中(income, deduct, rate)。要想修改设计，将任意的绑定限定在闭包之中，也非常简单。只是为了好玩，在本例子中我们也使用了两种稍微不同的函数式风格。第一种风格连续将多个值绑定到了闭包的作用范围；通过允许taxFP成为可变的变量，这些“添加绑定”的代码行可以任意顺序出现。然而，如果我们想要使用tax_with_Income这样的不可变名字，我们就需要以特定的顺序来安排这几行进行绑定的代码，将靠前的绑定结果传递给下一个绑定。无论在哪种情况下，在全部所需数据都绑定进闭包范围之后，我们就可以调用“种子”（seeded）方法了。

第二种风格在我看来，更象是Lisp（那些括号最象了）。除去美学问题，这第二种风格有两点值得注意。第一点就是完全避免了名字绑定，变成了一个单个的表达式，连语句都没有使用（关于为什么不使用语句很重要，请参见 P第一部分）。
第二点是闭包的“Lips”风格的用法和前文给出的“Smalltalk”风格的信息传递何其相似。实际上两者都在调用taxdue()函数/方法的过程中积累了所有值(如果以这种原始的方式拿不到正确的数据，两种方式都会出错）。“Smalltalk”风格的方法中每一步传递的是一个对象，而“Lisp”风格的方法中传递是持续进行的。 但实际上，函数式编程和面向对象式编程两者旗鼓相当。

'''