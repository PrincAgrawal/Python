# what are sets
x = {"prince", "mohit", "aman", "harshita", "naman"}
print(x)

# set unordered hota hai
# unchangable
# unindexed -> index ke through kisi bhi item ko access nhii kr skte

# duplicate not allowed
x = {"a", "b", "c", "a"}
print(x)

# get the length of the set
print(len(x))

# how to check the data type of the set
print(type(x))


# a set with string , integer and boolean means all data type
x = {"prince", True, 67, "male"}
print(x)


# the set() constructor
myset = set(("a", "b", "c"))
print(myset)


# how to access items in set
prince = {"a", "b", "c"}
for i in prince:
    print(i)


# check if banana is present or not
x = {"apple", "banana", "papaya", "kiwi"}
print("banana" in x)


# adding set items
x = {"apple", "banana", "papaya", "kiwi"}
x.add("orange")
print(x)


# how to add items from another set into the current set
x = {"apple", "banana", "papaya", "kiwi"}
y = {"pineaple", "mango", "graps"}
x.update(y)
# x.intersection(y)
print(x)


# how to remove set items
x = {"apple", "banana", "papaya", "kiwi"}
x.remove("apple")
print(x)


# how to use discard() for removing the items in set
x = {"apple", "banana", "papaya", "kiwi"}
x.discard("apple")
print(x)

x.clear()
print(x)

# how to join the two sets by union()
set1 = {"apple", "banana", "papaya", "kiwi"}
set2 = {"pineaple", "mango", "graps"}
set3 = set1.union(set2)
print(set3)

# how to join the two sets by update()
set1 = {"apple", "banana", "papaya", "kiwi"}
set2 = {"pineaple", "mango", "graps"}
set1 = set1.union(set2)
print(set1)


# keep only duplicate items intersection_update()
set1 = {"apple", "banana", "papaya", "kiwi"}
set2 = {"pineaple", "mango", "graps", "banana"}
set1.intersection_update(set2)
print(set1)


# intersection()
# symetric_difference_update()


# All python Built in set methods
# add()
# clear()
# copy()
# difference()
# difference_update()
# discard()
# intersection()
# intersection_update()
# pop()
# remove()
# union()
# update()
# symmetric_difference()
# symmetric_difference_update()
