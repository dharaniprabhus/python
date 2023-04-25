import time

def say(text):
    def inner(func):
        def wrapper(*args,**wargs):
            print(f"{text}")
            val = func(*args,**wargs)
            print(f"{val}")
            return val
        return wrapper
    return inner

class CallCounter:
    def __init__(self,func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f"self.func.__name__ called {self.counter} times")
        return self.func(*args,**kwargs)

@say("Hello!!!")
@say("World!!!")
def add(a,b):
    return a+b

# class decorator
def mark(cls):
    cls.attr = "Decorated"
    cls.add = add
    return cls

@mark
class Test:
    pass

@CallCounter
def mult(a,b):
    return a*b

add (4,5)
for i in range(4):
    print(mult(4,5))

DEBUG = True
## ex 3.7.1
def measure(n):
    def inner(func):
        if not DEBUG:
            return func
        def wrapper(*args, **kwargs):
            sum = 0
            for _ in range(int(n)):
                start = time.perf_counter()
                result = func(*args,**kwargs)
                elapsed = time.perf_counter() - start
                sum += elapsed
            print("total elapsed time : ",sum)
            print("avg elapsed time : ",float(sum)/n)
            return result
        return wrapper
    return inner

@measure(12343545)
def exp(a):
    return pow(2,a)

print("Pow is ", exp(4))
