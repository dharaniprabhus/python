# square
res = [x**2 for x in range(10,51) if x % 2 == 0]
print(res)


# float of 3d points
xcoord = [x/10 for x in range(1,4)]
ycoord = [y/10 for y in range(1,6)]
zcoord = [z/10 for z in range(1,2)]

threed_points = [(x,y,z) for x in xcoord for y in ycoord for z in zcoord]
print(threed_points)

#dict
d = {x**2:x for x in range(10)}
print(d)


#dict generator
gen = ((x**2,x) for x in range(10))
d = dict(gen)
print(d)


#set 
s = {abs(x) for x in [-3, -4, 10, 5]}
print(s)

#set generator exp
gen = (abs(x) for x in [-3, -4, 10, 5])
s = set(gen)
print(s)
