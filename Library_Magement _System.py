class Library:
    def __init__(self, BookName="", Writer=""):
        self.BookName = BookName
        self.Writer = Writer

    def Book_Name(self):
        self.BookName = input("Enter Book Name: ")

    def Book_writer(self):
        self.Writer = input("Enter Book Writer: ")
    
    def Show_Book_Details(self):
        """Prints book name and writer"""
        print(f"{self.BookName} written by {self.Writer}")

    @staticmethod
    def include_books():
        """Static method to include books"""
        pass

# Creating a Library object and setting its attributes using methods

Book1 = Library()
Book1.Book_Name()
Book1.Book_writer()
Book1.Show_Book_Details()
