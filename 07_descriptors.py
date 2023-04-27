import math

# approach 1
class Square:
    def __init__(self,side):
        self.side = side

    def my_get(self):
        """ area of square """
        return self.side*2

    def my_set(self,value):
        self.side = math.sqrt(value)

    def my_del(self):
        print("Cannot delete the area")

    area = property(fget=my_get,fset=my_set,fdel=my_del,doc=my_get.__doc__)

# approach 2
class Circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @area.setter
    def area(self, value):
        self.radius = math.sqrt(value / math.pi)

c = Circle(4)
print(c.area)
c.area = 24
print(c.radius)

# internals

class DataDescriptor:
    def __init__(self,value):
        self.value = value

    def __get__(self,instance,cls):
        print("__get__")
        return self.value

    def __set__(self,instance,value):
        print("__set__")
        self.value = value

class WithDescriptor:
    attr = DataDescriptor(4)

w = WithDescriptor()
w.attr
w.attr = 5
print(w.attr)
print(w.__dict__)

class NonDataDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, cls):
        print("non data __get__")
        return self.value

class WithNonDescriptor:
    attr = NonDataDescriptor(4)

w = WithNonDescriptor()
w.attr
print(w.attr)
w.attr = 5
print(w.attr)
print(w.__dict__)
