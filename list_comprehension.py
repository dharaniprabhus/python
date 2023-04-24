# Motivation readable, expressive

# From existing list
def even():
    numbers = [1,2,3,4,5,6]
    return [x for x in numbers if x%2 == 0]

# From custom iterator
class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current

def odd():
    numbers = MyIterator(0,10)
    return [x for x in numbers if x%2==1]

# From string
def vowel_in_string(inp):
    vowels = ['a','e','i','o','u']
    return [c for c in inp if c in vowels]

# dict comprehension
def square():
    numbers = MyIterator(0,10)
    sq = {n : n*n for n in numbers}
    return sq

li = [x.upper() for x in "DharaNI"]
print(li)

li = [(x, y) for x in range(4) for y in range(5, 10)]
print(li)

d = {x: x.upper() for x in "dhrani"}
print(d)

# swap
d = {v: k for k, v in d.items()}
print(d)

print(even())
print(odd())
print(vowel_in_string("hello"))
print(square().get(4))
