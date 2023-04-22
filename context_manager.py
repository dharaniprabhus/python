import time

class Timer:
    def __enter__(self):
        self.start = time.monotonic()

    def __exit__(self,exc_typ,exc_val,traceback):
        elapsed = time.monotonic() - self.start
        print(f"Elapsed time: {elapsed:.6f} seconds")

def fib(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fib(val-1) + fib(val-2)

with Timer():
    print(fib(35))
