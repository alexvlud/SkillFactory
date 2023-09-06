class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"Circle: {self.x}, {self.y}, {self.r}"

    def get_area(self):
        return 3.14*(self.r**2)







