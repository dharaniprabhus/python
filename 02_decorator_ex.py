import functools
import time

class MyClass:
    def foo():
        print("foo called!")

    foo = staticmethod(foo)


# using standard decortors
class MyclassDecorator:
    @staticmethod
    def foo():
        print("foo called!")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # called when __str__ does not exist
    # dunder methods
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x},{self.y})"

    def __str__(self):
        return f"str {self.__class__.__name__}({self.x},{self.y})"

    @staticmethod
    def create_point(x,y):
        return Point(x,y)

    @classmethod
    def clone_point(cls,point):
        return cls(point.x,point.y)

# closure
def outer(a):
    a.append(30)
    def inner(b):
        sum = 0
        for v in a:
           sum += v
        sum += b
        return sum
    return inner

# decorator
def hello(func):
    #TODO how to get the documentation
    @functools.wraps(func)
    def inner(*args,**kwargs):
        val = func(*args,**kwargs)
        return f"Hello {val}"
    return inner


def measure(func):
# sum = 0.0
    def inner(*args,**kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        elapsed = time.perf_counter()-start
# sum += elapsed
        print(f"measure {elapsed}")
        return val
    return inner

@hello
def add(a,b):
    """ Add two numbers """
    return a + b


def fcache(func):
    d = {}
    def inner(n):
        if n not in d:
            d[n] = func(n)
        return d[n]
    return inner


def _fib(n):
    """Calculate fibonacci number slow"""
    if n <= 2:
        return 1
    return _fib(n - 1) + _fib(n - 2)

# @fcache
@measure
def fib(n):
    val = _fib(n)
    return val

@functools.cache
def fib2(n):
    """Calculate fibonacci number slow"""
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_fast(n):
    """Calculate fibonacci number fast"""
    if n <= 2:
        return 1
    p, q = 1, 1
    for _ in range(n - 2):
        p, q = q, p + q
    return q


obj = MyClass()
obj.foo()
obj = MyclassDecorator()
obj.foo()
MyclassDecorator.foo()
p = Point(2,3)
print(p)
p = Point.create_point(3,4)
print(p)
p2 = Point.clone_point(p)
print(p2)

val = [10,20]
obj = outer(val)
print("inner " , obj(20))
print("val " , val)
print(add(4,10))

print(fib(37))
# print(fib2(35))
# help(add)
