def countup(start, end, step):
    s = start
    while (s+step) < end:
        s += step
        yield s

for i in countup(3,44,5):
    print(i)

def init_coroutine(func):
    def wrapper(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen

    return wrapper

@init_coroutine
def co_countup():
    step = None
    step = yield

    e = 100
    s = 0
    while (s + step) < e:
        s += step
        yield s


gen = co_countup()
gen.send(3)
for i in gen:
    print(i)
