# globar variable
x = 90


def myfunc():
    y = 98
    print(x)


myfunc()


def myfunc2():
    x = 48
    print(x)
    myfunc()


myfunc2()


# global keyword - if you need to create a global variable locally then you should use global keyword.
x = 90898


# if we want to change the global variable inside the function we can do it using global keyword inside that function
def sharad():
    global x
    x = 970


sharad()
print(x)
