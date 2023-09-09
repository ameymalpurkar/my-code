class determinant():
    def __init__(self):
        self. a = "a" 
        self. b = "b"
        self. c = "c"
        self. d = "d"

    def get_determinant(self, a, b, c, d):
        return (a*c)-(b*d)
    
def main():
    a = (int(input("Enter the value of a: ")))
    b = (int(input("Enter the value of b: ")))
    c = (int(input("Enter the value of c: ")))
    d = (int(input("Enter the value of d: ")))

    calculate = determinant()
    print("the answer is "(calculate.get_determinant(a, b, c, d)))

if __name__ == "__main__":
    main()
