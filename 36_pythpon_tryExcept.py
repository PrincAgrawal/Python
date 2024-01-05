# try - block let you test a block of code for error
# except - block lets you handle the error
# else -block lets you execute the code when there is no error
# finally - block lets you know execute the code regardless of these

# example of try block
"""try:
    print(x)
except:
    print("an error occured")


# many exceptions - you can even define many exception block
try:
    print(x)
except NameError:
    print("variable of x is not defined")
except:
    print("something else went wrong")"""

x=67

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")


# finally -
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try' except is finished")


# example
try:
    f = open("input.txt")
    try:
        f.write("Prince Agrawal")
    except:
        print("something went wrong then write into the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")


# raise an exception
x = -1
if x < 0:
    raise Exception("sorry , no number is below 0")
