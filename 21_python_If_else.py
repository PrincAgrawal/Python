# python condtion and if statement
a = 90
b = 76

# example of if statement ->
if a > b:
    print("a is grater than b")


# the Elif keyword
a = 77
b = 77
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is greater than b")


# else keyword
a = 45
b = 67
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is greater than b")
else:
    if b > a:
        print("b is greater than a")
    else:
        print("wow")


# with logical operator
a = 300
b = 88
c = 90
if a > b and c > a:
    print("both the conditions are true")


# the pass statement  - if with any reason if statement has no content than you canpass the statement for avoiding the error in program
a = 33
b = 200
if a > b:
    pass
