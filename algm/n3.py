__author__ = 'Administrator'
from typing import Iterator, typevar, Generic, Function, List

T = typevar('T')

def example_typed(x : Iterator[int]) -> Iterator[str]:
    for i in x:
        yield str(i)

def example_generic(x : Iterator[T]) -> Iterator[T]:
    for i in x:
        yield i

a = typevar('a')
b = typevar('b')

class Functor(Generic[a]):
    def __init__(self, xs : List[a]) -> None:
        self._storage = xs

    def iter(self) -> Iterator[a]:
        return iter(self._storage)


def fmap(f : Function[[a], b], xs : Functor[a]) -> Functor[b]:
    return Functor([f(x) for x in xs.iter()])



class Monad(Generic[a]):
    def __init__(self, val : a) -> None:
        self.val = val


class IdMonad(Monad):

    # Monad m => a -> m a
    def unit(self, x : a) -> Monad[b]:
        return IdMonad(x)

    # Monad m => m a -> (a -> m b) -> m b
    def bind(self, x : Monad[a], f : Function[[a], Monad[b]]) -> Monad[b]:
        return f(x.val)

    # Monad m => m (m a) -> m a
    def join(self, x : Monad[Monad[a]]) -> Monad[a]:
        return x.val