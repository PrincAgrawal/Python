# Iterator is an object which implement the iterator protocol , which consist of the 2 methods: __iter__()  and  __next__()

# iterators Vs iterable
# all of the 4 data type i.e - list, set, dicyionary and tuples are iterators
# iterators methods

sharad = ("prince", "agrawal", "mohit", "aman")
isharad = iter(sharad)
print(next(isharad))
print(next(isharad))
print(next(isharad))
print(next(isharad))


# a new example
sharad = "banana"
datacode = iter(sharad)
print(next(datacode))
print(next(datacode))
print(next(datacode))
print(next(datacode))
print(next(datacode))
print(next(datacode))


# looping through an iterator
names = ["prince", "mohit", "aman"]
for i in names:
    print(i)


# create an iterator
# to create an object or class you will have to implement
# __iter__() and __next__() to the object.

# all classses have a function which is called __init__().
# which allows you to some initialization

# example for better understanding


class mynumber:
    def __iter__(self):
        self.a = 3
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = mynumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# stopiteration - to prevent the iteration to go over
# forever , we se the stopiteration statement


class mynumber:
    def __iter__(self):
        self.a = 3
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = mynumber()
myiter = iter(myclass)
for i in myiter:
    print(i)
