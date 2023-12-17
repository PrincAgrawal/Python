# file handling - open()
f = open("demofile.txt")

# or
f = open("demofile.txt", "rt")  # rt- read text

# there are 4 different modes of opening file
#  "r","a","w","x"

# to open the file using built in open()and read()
f = open("demofile.txt", "r")
print(f.read())


# open a file different in locaion
f = open("D:\prince.txt.txt", "r")
print(f.read())

# read only parts of the file
f = open("D:\prince.txt.txt", "r")
print(f.read(7))


# how to read lines
f = open("D:\prince.txt.txt", "r")
print(f.readline())
print(f.readline())

print()
# looping through the line by line
f = open("D:\prince.txt.txt", "r")
for i in f:
    print(i)

# how to close the open file
f = open("D:\prince.txt.txt", "r")
print(f.readline())
# print(f.close())
