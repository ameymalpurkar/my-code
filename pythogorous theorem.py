a = (int(input("Enter the number1\n")))
b = (int(input("Enter the number2\n")))
c = (int(input("Enter the number3\n")))

if a*a == b*b + c*c :
    print("yes , This numbers are a Pythagorean Triplet")

elif b*b == a*a + c*c:
    print("yes , This numbers are a Pythagorean Triplet")

elif c*c == a*a + b*b:
     print("yes , This numbers are a Pythagorean Triplet")
     
else:
    print("No , This numbers are not a Pythagorean  Triplet")