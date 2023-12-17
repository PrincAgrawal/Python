# regex - regular expression, is a sequence of characters that forms a search pattern.
# regEx module

import re

txt = "the rain is falling in india"
x = re.search("^the.*india$", txt)
if x:
    # pass
    print("yes match is true")
else:
    # pass
    print("no match")

    # regex functions
    # findall()
    # search()
    # split()
    # sub()

    # Metacharacters
    # \d - escape character
    # .  - any character(except new line character)
    # $  - ends with
    # *  - zero or more occurence
    # +  - one or more occurence
    # ?  - zero or one occurence
    # {} - exactly the specified number of occurence
    # |  - either or
    # () - capture and group

    # the findall() function
import re

txt = "my rain in spain"
x = re.findall("in", txt)
print(x)


# if in findall no condition is given the it will show empty list.
import re

txt = "my rain in spain"
x = re.findall("india", txt)
print(x)

# the search() function
txt = "the rain in spain"
x = re.search("\s", txt)
print("white space is located in ", x.start())


# when nothing found in search function
import re

txt = "my rain in spain"
x = re.findall("india", txt)
print(x)


# the split() function
import re

txt = "the rain in spain"
x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)


# the sub() function - replaces the mathches with the txt of your choice
txt = "the rain in spain"
x = re.sub("\s", "@", txt)
print(x)
