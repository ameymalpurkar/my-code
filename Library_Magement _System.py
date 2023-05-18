''' code created by Amey '''
# class LIbrary with some other functions
class Library:
    # constructor for the Instances named as "BookName" , "Writer"
    def __init__(self, BookName="", Writer=""):
        self.BookName = BookName
        self.Writer = Writer

    # function to allow user to prompt its Book's name
    def Book_Name(self):
        self.BookName = input("Enter Book Name: ")
     
    # function to allow user to prompt its Book's Writer
    def Book_writer(self):
        self.Writer = input("Enter Book Writer: ")

    # function is for getting  details of book 
    def Show_Book_Details(self):
        """Prints book name and writer"""
        print(f"{self.BookName} written by {self.Writer}")

    # static method for printing the books with no error
    @staticmethod
    def include_books():
        """Static method to include books"""
        pass




# actual interface code written for interacting with user

Book1 = Library()
Book1.Book_Name()
Book1.Book_writer()
Book1.Show_Book_Details()




