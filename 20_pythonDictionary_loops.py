x = {"brand": "ford", "model": "xyz", "year": 2023}

for i in x:
    print(i)


# with looping print all the values in the dictionary , one by one
x = {"brand": "ford", "model": "xyz", "year": 2023}

for i in x:
    print(x[i])

# values() method  to return values of a dict
x = {"brand": "ford", "model": "xyz", "year": 2023}
for i in x.values():
    print(i)

print()
# keys() method to return the key of the dict
x = {"brand": "ford", "model": "xyz", "year": 2023}
for i in x.keys():
    print(i)

print()
# now loop through both the keys and values , by using the item
x = {"brand": "ford", "model": "xyz", "year": 2023}
for i, y in x.items():
    print(i, "->", y)


# copy dictionary
x = {"brand": "TATA", "model": "xyz", "year": 2023}
y = x.copy()
print(y)


# nested dictionary
myfamily = {
    "child1": {"name": "prince", "year": "19"},
    "child2": {"name": "mohit", "year": "18"},
    "child3": {"name": "aman", "year": "20"},
}
print(myfamily)
