from python.session4.modulos import CircleMethods


def calculateAreaPerimeterCircle():
    radius = float(input("Set the Radius : "))
    print("The Area of the circle is: ", CircleMethods.circleArea(radius))
    print("The Perimeter of the circle is: ", CircleMethods.perimeterCircle(radius))


calculateAreaPerimeterCircle()
