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
