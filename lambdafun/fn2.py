__author__ = 'Administrator'
'''
一个对象就是附有若干过程（procedure）的一段数据。。。
一个闭包（closure）就是附有一段数据的一个过程（procedure）。
'''

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

