# what is a module
# consider a  module to be as same as a code library like a  file containing functions you want to include in a application
import myModule

myModule.greetings("Prince Agrawal")


# variable in module
# a module can contain functions but also variables of all types
import myModule1

a = myModule1.person["age"]
print(a)


# naming and re-naming a module with as keyword
import myModule1 as mx

a = mx.person["age"]
print(a)

# konsa platform use kr rhe hai uske liye
import platform

x = platform.system()
print(x)


# using dir() function
import platform

x = dir(platform)
print(x)


# import from module - you can choose to import only parts of a module

from myModule2 import person1

print(
    person1["age"]
)  # do not write like "x=myModule2.person2["age"]" when you use from keyword to import module
