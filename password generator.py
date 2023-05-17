import string
import random 
a.Generatorpassbank
def Generatorpassbank ():
    Password_Length = int(input("enter the password length\n"))
    print(Password_Length)
    if Password_Length == int:
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.punctuation
        s4 = string.digits
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        print("".join (random.sample(s,Password_Length)))
    
    else:
        print("your value is not correct")
