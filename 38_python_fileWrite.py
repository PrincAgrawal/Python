# 2 modes for writing in the file
# "a" , "w"
f = open("demofile.txt", "a")
f.write(" wow, Now this file has one more content")
f.close()

# open and read the file after the appending
f = open("demofile.txt", "r")
print(f.read())


# 1st open the file aand overwrite the correct
f = open("demofile.txt", "w")
f.write("Maine sab delete kr diya hai acchi baat hai wow...!!")
f.close()


# open and read the file after the appending
f = open("demofile.txt", "r")
print(f.read())


# creating a new file
#  "x" - create a file
#  "a" - append file
# "w" - wil write or create a file
#  "r" - will read the file

f = open("myfile.txt", "x")
f.close()
# how to delete a file
import os

os.remove("myfile.txt")


# check if the file exist and give the condition'
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("file doesn't exist")
