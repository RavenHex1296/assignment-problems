import matplotlib.pyplot as plt


class Shape:
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color

    def describe(self):
        print(
            "Base: {}\nHeight: {}\nColor: {}\nPerimeter: {}\nArea: {}\nVertices: {}".format(
            self.base, self.height, self.color,
            self.perimeter, self.area, self.vertices))

    def render(self):
        x = []
        y = []
        for pairs in self.vertices:
            x.append(pairs[0])
            y.append(pairs[1])

        x.append(0)
        y.append(0)
        plt.clf()
        plt.style.use('bmh')
        plt.gca().set_aspect("equal")
        plt.plot(x, y, color=self.color, linewidth=2.5)
        plt.savefig(self.__class__.__name__+".png")


class Rectangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)
        self.perimeter = 2 * base + 2 * height
        self.area = base * height
        self.vertices = [(0, 0), (base, 0), (base, height), (0, height)]


class Triangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)
        self.perimeter = base + height + (base ** 2 + height ** 2) ** 0.5
        self.area = base * height / 2
        self.vertices = [(0, 0), (base, 0), (0, height)]


class Square(Rectangle):
    def __init__(self, base, color):
        super().__init__(base, base, color)

print("Asserting Rectangle")
rect = Rectangle(5, 2, "red")
rect.describe()
rect.render()

print("Asserting Triangle")
tri = Triangle(5, 2, "blue")
tri.describe()
tri.render()

print("Asserting Square")
sq = Square(5, "green")
sq.describe()
sq.render()
