__author__ = 'Administrator'
class TaxCalc:
    def taxdue(self):return (self.income-self.deduct)*self.rate
taxclass = TaxCalc()
taxclass.income = 50000
taxclass.rate = 0.30
taxclass.deduct = 10000
print"Pythonic OOP taxes due =", taxclass.taxdue()