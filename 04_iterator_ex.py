class OneDirIterator:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.counter = start
    
    def __next__(self):
        counter = self.counter
        if counter == self.end:
            raise StopIteration
        self.counter += 1
        return counter

    def __iter__(self):
        print("__iter__ called")
        self.counter = self.start
        return self


for i in OneDirIterator(4,8):
    print(i)

# would need to handle exception when next(it) is called
it = OneDirIterator(15,16)
try:
    print(next(it))
except StopIteration:
    pass
