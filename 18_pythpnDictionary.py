# definition of dictionary -->
sharad = {"brand": "ford", "model": "dt", "year": 2020}
print(sharad)


# if you want to print "brand" value from the dictionay
sharad = {"brand": "ford", "model": "dt", "year": 2020}
print(sharad["brand"])

# duplicate not allowed
sharad = {"brand": "ford", "model": "dt", "year": 2020, "year": 2023}
print(sharad)


# how to find dictionary length
sharad = {"brand": "ford", "model": "dt", "year": 2020, "year": 2023}
print(len(sharad))


# dictionary items - data types
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
print(sharad)
print(type(sharad))

# accessing items of dictionary
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}

x = sharad["model"]
print(x)


# accessing items through get() function
sharad = {
    "brand": "ford",
    "model": "DT",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
x = sharad.get("model")
print(x)


# key() method will return all the keys in the dictionary
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
x = sharad.keys()
print(x)

# key() method will return all the keys values in the dictionary
x = sharad.values()
print(x)

# adding items to the original dictionary
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
x = sharad.keys()
print(x)  # before the change
sharad["color"] = "white "
print(x)  # after the change
x = sharad.values()
print(x)

x = sharad.items()
print(x)


# check if the key exists
sharad = {
    "brand": "ford",
    "model": "dt",
    "year": 2020,
    "color": ["red", "white", "blue"],
}
if "model" in sharad:
    print("yes,'model' is present in the sharad")
