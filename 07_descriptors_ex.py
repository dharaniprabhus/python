class PositiveNumber:
    def __init__(self):
        self.value = None
        self.name = None

    def __set_name__(self,owner,name):
        self.name = "_" + name

    def __get__(self,instance,cls):
        value = getattr(instance,self.name)
        return round(value,2)

    def __set__(self,instance,value):
        if (value < 0):
            raise ValueError("Positive number expected")
        setattr(instance,self.name,value)

class Speed:
    kmh = PositiveNumber()

    def print(self):
        print(self.kmh)
        

s = Speed()
s.kmh = 3.5234234
s.print()
s2 = Speed()
s2.kmh = 4.3243
s2.print()
