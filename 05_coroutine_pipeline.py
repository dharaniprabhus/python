def show_upper():
    while True:
        text = yield
        print(text.upper())

gen = show_upper()
gen.send(None)
gen.send("Hello")
gen.send("World")


def init_coroutine(func):
    def wrapper(*arg,**kwarg):
        gen = func(*arg,**kwarg)
        next(gen)
        return gen
    return wrapper


@init_coroutine
def show_upper2():
    res = None
    try:
        while True:
            text = yield res
            res = text.upper()
    except GeneratorExit:
        print("Close called! generator done.")

gen = show_upper2()
gen.send("Hello2")
gen.close()


# pipeline
import random
import time
import io
from threading import Thread, Lock
fobj = io.StringIO()
lock = Lock()
def log():
    while True:
        value = random.randrange(0, 100)
        with lock:
            if value < 10:
                fobj.write("# comment\n")
            else:
                fobj.write("%d\n" % value)
        time.sleep(0.2)


t = Thread(target=log)
t.start()

@init_coroutine
def printer():
    while True:
        line = yield
        print(f"sum = {line}")

@init_coroutine
def _sum(p):
    s = 0
    while True:
        line = yield
        s += int(line)
        p.send(s)

@init_coroutine
def remove_comments(s):
    while True:
        line = yield
        if not line.startswith("#"):
            s.send(line)

p = printer()
s = _sum(p)
gen = remove_comments(s)

rpos = 0
while True:
    line = None
    fobj.seek(rpos)
    with lock:
        line = fobj.readline().strip()
        rpos = fobj.tell()
        if len(line):
            gen.send(line)
    time.sleep(.1)

gen.close()
t.join()

