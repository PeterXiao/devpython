__author__ = 'Administrator'
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
      TaxCalc().setIncome(50000).setRate(0.30).setDeduct(10000).taxdue()
	  
"""
	  每个"setter"方法都返回self可以让我们将每个方法调用的结果当作“当前”对象进行处理。
	  这和FP中的闭包方式有些相似。
	  """