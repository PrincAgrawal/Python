# regex - regular expression, is a sequence of characters that forms a search pattern.
# regEx module

import re

txt = "the rain is falling in india"
x = re.search("^the.*india$", txt)
if x:
    pass
    # print("yes match is true")
else:
    pass
    # print("no match")

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

    txt = "the rain in spain"
    x = re.search("\s", txt)
    print(x)
