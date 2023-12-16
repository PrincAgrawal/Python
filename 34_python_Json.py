# Json is a syntax for storing and exchanging the data , it is text which is written with javascript object notations.

# comverting from json to python
import json

x = '{"name": "Prince", "Age": 45, "City": "Jaipur"}'
y = json.loads(x)
# the result will be python dictionary
print(y["Age"])


# converting from python to json
import json

x = {"name": "Prince", "Age": 45, "City": "Jaipur"}
y = json.dumps(x)
# the result will be in string
print(y)
