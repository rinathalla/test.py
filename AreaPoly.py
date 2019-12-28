class Shape:
    width = 0
    height = 0


def area(self):
    print("Parent Class")


class Rectangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print("area of rectangle", self.width * self.height)


class Triangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print("area of rectangle", (self.width * self.height) / 2)


rectangle = Rectangle(10, 20)
triangle = Triangle(20, 15)

rectangle.area()
triangle.area()
