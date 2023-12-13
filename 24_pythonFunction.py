# creating and calling a function


def my_func():
    print("My name is Prince Agrawal....!!")


my_func()


def my_func(fname):
    print(fname + "Agrawal ")


my_func("Prince ")
my_func("Mohit ")
my_func("Aman ")


# number of arguments
def my_func(fname, lname):
    print(fname + " " + lname)


my_func("Prince", "Agrawal")


# Arbitrary arguments , *args
def my_func(*kids):
    print("the youngest child is " + kids[0])


my_func("Prince", "Mohit", "Aman")


# keyword arguments key=value
def my_func(child1, child2, child3):
    print("The youngest child is " + child3)


my_func(child1="Prince", child2="Mohit", child3="Aman")


# arbitrary keyword arguments  **kwargs
def my_func(**kids):
    print("his last name is " + kids["lname"])


my_func(fname="sharad", lname="Agrawal")


# default paraeter value
def my_func(country="India"):
    print(" I am from " + country)


my_func("UK")
my_func("US")
my_func()
my_func("Canada")

print()


# passing a list as an argument
def my_func(food):
    for i in food:
        print(i)


name = ["prince", "mohit", "aman"]
my_func(name)


print()


# return values from the function
def my_func(x):
    return 5 * x


print(my_func(6))
print(my_func(3))
print(my_func(9))


# the pass statement
def my_func(x):
    pass


my_func(9)
