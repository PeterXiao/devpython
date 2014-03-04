__author__ = 'Administrator'
from macropy.case_classes import case

@case
class Nil():
    pass

@case
class Cons(x, xs):
    pass

Cons(1, Cons(2, Cons(3, Nil())))