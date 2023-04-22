import itertools

num = [1,2,3, 4]
fruits = ["apple","bananna","cherry", "avacado"]
colors = ["red","yellow", "black", "green"]

# example chain
for i in itertools.chain(num,fruits,colors):
    print(i)


#example group
groups = itertools.groupby(sorted(fruits), key=lambda x: x[0])
for key,val in groups:
    print(key, list(val))
