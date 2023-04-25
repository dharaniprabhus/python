import itertools

# cycle
three_cycle = itertools.cycle([1,2,3])
for i in range(10):
    print(next(three_cycle))

# count
for i in itertools.count(1,3):
    if i == 10:
        break
    print(i)

# repeat
repeat = itertools.repeat(6,4)
for _ in range(4):
    print(next(repeat))

# accumulate
acc = itertools.accumulate([1,2,3,4,5])
for v in acc:
    print(v)

# normal zip
x = [1,2,3]
y = [3,4]
z = [4]
for v in zip(x,y,z):
    print(v)

#zip longest
x = [1,2,3]
y = [3,4]
z = [4]
zl = itertools.zip_longest(x,y,z)
for v in zl:
    print(v)

seq = [4,12,99,23,45,98,356, 2]
ans = list(x+y for x,y in itertools.pairwise(seq))
print(ans)

print(seq)
print(list(zip(seq[:-1],seq[1:])))
