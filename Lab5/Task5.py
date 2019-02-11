class Test_point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def pnt(self):
        print("x =", self.x)
        print("y =", self.y)

point = Test_point()
point.pnt()

point = Test_point(10)
point.pnt()

point = Test_point(20, 30)
point.pnt()

#String method
class Test_point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

point = Test_point()
print(point)

point = Test_point(10)
print(point)

point = Test_point(10, 15)
print(point)

#third part
class Test_point(object):
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
         
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
         
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_point = Test_point(new_x, new_y)
        return new_point
         
point1 = Test_point(1, 3)
point2 = Test_point(4, 5)
 
print(point1 + point2)
