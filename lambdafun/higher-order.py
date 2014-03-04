__author__ = 'Administrator'
def foo_factory():
   def foo():
      print "Foo function from factory"
   return foo

f = foo_factory()

f()