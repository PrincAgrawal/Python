# loop through list
list = ["prince", "harshita", "mohit", "aman"]
for i in list:
    print(i)


print()
# loop through indexing
list = ["prince", "harshita", "mohit", "aman"]
for i in range(len(list)):
    print(list[i])


print()
# using a while loop
list = ["prince", "harshita", "mohit", "aman"]
i = 0
while i < len(list):
    print(list[i])
    i = i + 1

print()
# looping using list comprehension
list = ["prince", "harshita", "mohit", "aman"]
[print(i) for i in list]  # ise use nhii krte hai....


# list comprehension

fruits = ["payaya", "banana", "kela", "kivi", "cherray"]
newlist = []
for i in fruits:
    if "a" in i:
        newlist.append(i)
print(newlist)
