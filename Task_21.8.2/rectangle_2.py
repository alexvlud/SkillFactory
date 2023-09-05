from rectangle import Rectangle, Square, Circle

rect1 = Rectangle(3,4)
rect2 = Rectangle(12,5)

print(f"площадь прямоуг 1 = {rect1.get_area()}")
print(f"площадь прямоуг 2 = {rect2.get_area()}")

square1 = Square(5)
square2 = Square(10)

print(f"площадь квадр 1 = {square1.get_area_square()}")
print(f"площадь квадр 2 = {square2.get_area_square()}")

circle1 = Circle(6)
circle2 = Circle(9)
print(f"площадь окруж 1 = {circle1.get_area_circle()}")
print(f"площадь окруж 2 = {circle2.get_area_circle()}")


figures = [rect1, rect2, square1, square2, circle1, circle2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())

