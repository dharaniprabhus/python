# Motivation readable, composable, one-time usage
# syntax is is simillar to tuples
# valies are computed on the fly

# e.g.
def even(start,end):
    start = start + 1 if start%2 == 1 else start
    while start < end:
        yield start
        start += 2


for e in even(3,22):
    print(e)

#composing generator expression
numbers = range(10)
cubes = (x**3 for x in numbers)

while True:
    try:
        print(next(cubes))
    except StopIteration:
        break

