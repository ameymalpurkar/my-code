# this a square class that performs all operations on square shape
class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side
    
    def area (self):
        return self.side * self.side
        
# this a square class that performs all operations on rectangle shape
class rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2*(self.length + self.width)
     
    def area (self):
         return self.length * self.width
    

    

# user choose the shape
shape_choice = (input("enter the shape's name/ s for square /r for rectange /c for circle \n"))

# user operations on square shape
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
        
# user operations on rectangle shape
if (shape_choice == "r"):
    choice = (input("what do you want to calculate . type /p for perimeter/ a for area \n"))
    if(choice == "p"):
        num1 = (int(input("enter the length of a recangle\n ")))
        num2 = (int(input("enter the width of a recangle\n ")))
        shape = rectangle(num1,num2)
        output = int(shape.perimeter())
        print(f" the perimeter of the rectangle of the length {num1}and width {num2} is {output}")

    else :
        num1 = (int(input("enter the length of a rectangle\n ")))
        num2 = (int(input("enter the width of a rectangle\n ")))
        shape = rectangle(num1,num2)
        output = int(shape.area())
        print(f" the area of the rectangle of the length {num1}and width {num2} is {output}")
