def count_down(n):
    start = n
    while start > 0:
        yield start
        start-=1

for i in count_down(10):
    print(i)

# dont resuse generator exp
# e.g. 
# cd = count_down(10) 
# 
# for in in cd:
#   pass
#
# for i in cd: #already exhausted
#   pass


def double_countdown1(val):
    for x in count_down(val):
        yield x
    for x in count_down(val):
        yield x

def double_countdown2(val):
    yield from count_down(val)
    yield from count_down(val)

for i in double_countdown1(3):
    print(i)

for i in double_countdown2(3):
    print(i)
