from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1.get_Area(), rect_2.get_Area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_Area_Square(), square_2.get_Area_Square())

circle_1 = Circle(4)
circle_2 = Circle(9)

print(circle_1.get_Circle(), circle_2.get_Circle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print('Площади прямоугольников:', figure.get_Area())
    elif isinstance(figure, Circle):
        print('Площади квадратов:', figure.get_Area_Square())
    else:
        print('Площади окружностей:', figure.get_Circle())