# Json is a syntax for storing and exchanging the data , it is text which is written with javascript object notations.

# comverting from json to python
import json

x = '{"name": "Prince", "Age": 45, "City": "Jaipur"}'
y = json.loads(x)
# the result will be python dictionary
print(y)


# converting from python to json
import json

x = {"name": "Prince", "Age": 45, "City": "Jaipur"}
y = json.dumps(x)
# the result will be in string
print(y)


# you can convert the following python object to json string
# dict , list,tuples,string ,int ,float , true,false,none


import json

print(json.dumps({"name": "Prince", "Age": 90, "Gender": "Male"}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("sharad", "khare")))
print(json.dumps("hello"))
print(json.dumps(34))
print(json.dumps(65.98))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# when you convert from pyton to json than python objects are converted into javascript json
import json

x = {
    "name": "sharad",
    "age": 89,
    "Gender": "Male",
    "Married": True,
    "Divoced": False,
    "Children": ("Prince", "Naman"),
    "pets": None,
    "cars": [
        {"model": "BMW 2023", "color": "Red"},
        {"model": "ford", "color": "Black"},
    ],
}

# converting into python
y = json.dumps(x)
print(y)


# how to format the result
import json

x = {
    "name": "sharad",
    "age": 89,
    "Gender": "Male",
    "Married": True,
    "Divoced": False,
    "Children": ("Prince", "Naman"),
    "pets": None,
    "cars": [
        {"model": "BMW 2023", "color": "Red"},
        {"model": "ford", "color": "Black"},
    ],
}

# using the 4 indents to make it easier to read
print(json.dumps(x, indent=4, sort_keys=True))
