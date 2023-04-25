import itertools

# ex1
itertools.count()

#ex2
l = list(itertools.islice(itertools.count(),2,5))
print(l)

#ex3
l = list(itertools.islice(itertools.count(),1,5))
print(l)
