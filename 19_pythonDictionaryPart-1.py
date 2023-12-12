sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
sharad["model"] = 2018
print(sharad)


# update() method
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
sharad.update({"year": "2019"})
print(sharad)


# how to add items in the dictionary
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
sharad["color"] = "red"
print(sharad)


# adding item with update() method
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
sharad.update({"color": "yellow"})
print(sharad)


# removing items from the dictionary
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
sharad.pop("model")
print(sharad)


# removing last inserted item
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
sharad.popitem()
print(sharad)


# del keyword removes the items with the specified key name
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
del sharad["model"]
print(sharad)

del sharad


# clear() method is used to empty the dictionary
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
sharad.clear()
print(sharad)
