import math

def cache(func):
    d = {}
    def wrapper(*args):#unpack
        if args in d:
            return d[args]
        else:
            d[args] = func(*args)
            return d[args]
    return wrapper

@cache
def raises(x,y):
    print("POW(%d,%d)",x,y)
    return math.pow(x,y)

print(raises(2,3))
print(raises(3,4))
print(raises(2,3))

