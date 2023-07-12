from cmath import sqrt

class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side
    
    def area (self):
        return self.side * self.side
        

class rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2*(self.length + self.width)
     
    def area (self):
         return self.length * self.width
    

class circle:
    def __init__(self, radius):
        self.radius = radius
        

    def circumference (self):
        return 2*22/7*self.radius
     
    def area (self):
         return 22/7* sqrt(self.radius)

# user choose the shape
shape_choice = (input("enter the shape's name/ s for square /r for rectange /c for circle \n"))

# square
if (shape_choice == "s"):
    choice = (input("what do you want to calculate . type /p for perimeter/ a for area \n"))
    if(choice == "p"):
        num1 = (int(input("enter the length of side of a square\n ")))
        print(num1)
        shape = Square(num1)
        output = int(shape.perimeter())
        print(f" the perimeter of the square of the length {num1} is {output}")

    else :
        num1 = (int(input("enter the length of side of a square\n ")))
        print(num1)
        shape = Square(num1)
        output = int(shape.areas())
        print(f" the area of the square of the length {num1} is {output}")
        
# circle
elif (shape_choice == "c"):
    choice = (input("what do you want to calculate . type /c for circumference / a for area \n"))
    if(choice == "c"):
        num1 = (int(input("enter the radius of a  circle \n ")))
        print(num1)
        shape = circle(num1)
        output = (circle.circumference())
        print(f" the circumference of a circle of radius {num1} is {output}")

    else :
        num1 = (int(input("enter the length of side of a circle\n ")))
        print(num1)
        shape = Square(num1)
        output = int(circle.areas())
        print(f" the area of the circe of radius c{num1} is {output}")

# rectangle
if (shape_choice == "s"):
    choice = (input("what do you want to calculate . type /p for perimeter/ a for area \n"))
    if(choice == "p"):
        num1 = (int(input("enter the length of side of a square\n ")))
        print(num1)
        shape = Square(num1)
        output = int(shape.perimeter())
        print(f" the perimeter of the square of the length {num1} is {output}")

    else :
        num1 = (int(input("enter the length of side of a square\n ")))
        print(num1)
        shape = Square(num1)
        output = int(shape.areas())
        print(f" the area of the square of the length {num1} is {output}")