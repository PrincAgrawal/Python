# creating a parent class
class parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = parent("prince", "agrawal")
x.printname()


# example of inheritance -->
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(
            fname, lname
        )  #  yeh wali line mujhe samjh me nhii aayi...kyu likhi hai yeh kya use hai iska
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear,
        )


obj = Student("prince", "agrawal", 2023)
print(obj.firstname)
print(obj.lastname)
print(obj.graduationyear)
obj.welcome()
