# create a class


class myclass:
    x = 9


print(myclass)


# create object
class myclass:
    x = 8


p1 = myclass()
print(p1.x)


# The  __int__() function
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = person("sharad", 36)

print(p1.name)
print(p1.age)


# object method
class person:
    def __init__(self, name, age):
        # hum self ki jagah kuch bhi veariable use kr skte hai
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello everyone my name is " + self.name)


p1 = person("sharad", 98)
p1.myfunc()
print(p1.name)
print(p1.age)


# how to modify object properties
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello everyone my name is " + self.name)


p1 = person("sharad", 89)
p1.age = 45
print(p1.age)


# delete object properties
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello everyone my name is " + self.name)


del p1.age
del p1
