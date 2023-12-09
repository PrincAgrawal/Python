x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
print(x)

# duplicates values
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
print(x[6])

# length of list --> x ke andar kitne items hai
print(len(x))

# List items - Data types
x=["a","b","c"]
y=[1,4,5,7,8,3,45]
z=[True,False]

# a list with multiple values
x=["prince",18,"male","B.tech",True]
print(type(x))


# the List() constructor
x=list(("prince",18,"male","B.tech",True))
print(x)


# python collections (Arrays)
# Four types of data types in python :
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

# how to Access items
x=["apple","banana","orange"]
print(x[2])
 
# Range of Indexes
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
print(x[2:5])

# negative indexing
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
print(x[-6:-1])

# leaving out the start value
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
print(x[:5])

# leaving out the start value
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
print(x[2:])

# how to check if the items Exists in List
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
if "prince" in x:
    print("yes,'apple' is in the list")


# change the item value of the list
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
x[1]="Rohit"
print(x)

# changing the range of items values in Lists in python
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
x[1:3]=["apple","mango"]
print(x)

# change of one value by replacing it with 2 values
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
x[1:2]=["mehul","vivek"]
print(x)

# change of two value by replacing it with 1 value
x=["prince","mohit","aman","harshita","teena","manju","jyoti","naman"]
x[1:3]=["raja"]
print(x)
