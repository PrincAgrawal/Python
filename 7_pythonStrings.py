x="prince"
y='prince'
print(x)
print(y)

# single line string
x="sharad"
print(x)

# multiline string
z='''Warning: PowerShell detected that you might be using a screen reader and has disabled PSReadLine for compatibility purposes. If you want to re-enable it, run 'Import-Module PSReadLine'.'''
# print(z)

# strings are Arrays
a="prince"
print(a[5])


# looping through the string
for x in "banana":
    print(x)


# string length
z="kyaa haal chal Bhaii"
print(len(z))


# check string 
txt="in this tutorial everything is free"
print("free" in txt)   #return bool value


# check string with if for user friendly
txt="in this tutorial everything is free"
if "free" in txt:
    print("yes ,'free' is present")


# check if free is not present
txt="in this tutorial everything is free"
print("sharad" not in txt)


# print only if "sharad" is not present
txt="in this tutorial everything is free"
if "sharad" not in txt:
    print("No,'sharad' is not present")



