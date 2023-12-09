# Append()
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
x.append("vidit")
# print(x)

# insert()
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
x.insert(1,"nikita")
# print(x)

# Extend()
x=["mango","pineapple","payaya"]
y=["apple","banana","orange"]
x.extend(y)
# print(x)


# remove list items
x=["mango","pineapple","payaya"]
x.remove("mango")
# print(x)

# remove specify index
x=["mango","pineapple","payaya"]
x.pop(1)
# print(x)

# remove last index without knowing the last
x=["mango","pineapple","payaya"]
x.pop()
# print(x)

# using del for specific index
x=["mango","pineapple","payaya"]
del x[0]
# print(x)

# Deleting the list completely
x=["mango","pineapple","payaya"]
del x
 

#  clear the list method
x=["mango","pineapple","payaya"]
x.clear()
print(x)