# sort the list alphabetically
list=["prince","harshita","mohit","aman"]
list.sort()
# print(list)

# sort the list numerically
x=[100,45,29,76,20,39,62,31]
x.sort()
# print(x)

# sorting the list in the descending order
list=["prince","harshita","mohit","aman"]
x.sort(reverse=True)
# print(list)

# sorting the list of numeric in the descending order
x=[100,45,29,76,20,39,62,31]
x.sort()
x.reverse()  # ese bhi kr skte hai
print(x)


# customize sort function
def myfunc(n):
    return abs(n-50)
x = [100,45,29,76,20,39,62,31]
x.sort(key=myfunc)
# print(x)



# how to copy a list
x=["prince","mohit","aman","harshita","rajkumar"]
# y=list(x) 
y=x.copy()
print(y)


# joining the list
x=["prince","mohit","aman","harshita","rajkumar"]
y=[2,4,5,7,9,4]
z=x+y
print(z)

# another way of joining through append()
x=["prince","mohit","aman","harshita","rajkumar"]
y=[4,6,7,34,2,6]

for i in y:
    x.append(i)

print(x)


# another way of joining through extend()
x=["prince","mohit","aman","harshita","rajkumar"]
y=[4,6,7,34,2,6]
x.extend(y)
print(x)


# list methods-->
    # append()
    # clear()
    # copy()
    # count()
    # extend()
    # index()
    # insert()
    # pop()
    # remove()
    # reverse()
    # sort()