# tuple aur list me yeh hi main diff hai ki tuple uneditable aur unchangable hota hai 
# tuple me duplicate allow hota hai
# ordered 

x=("Prince","Harshita","Simran","Abhishek","Mohit","Vipin")
print(x)
print(len(x))
print(type(x))

# craete tuple with one item 
x=("prince",)
print(type(x))

# not a tuple
x=("sharad")
print(type(x))

# tuple items _ data type(String , int , boolean)
x=("prince","harshita","aman","mohit")
y=(3,5,6,3,8)
z=(True,False,True)
print(x)
print(y)
print(z)


# tuple can alsocontain diff data type 
x=("prince",20,True,50,"male")
print(x)


# the tuple() constructor
sharad= tuple(("apple","banana","payaya"))
print(type(sharad))

# packing a tuple (when we assign a value to tuple)
x=("prince","aman","mohit")

# unpacking the tuple (when we extract the value from the tuple)
x=("prince","aman","mohit")
(green,red,yellow)=x
print(green)
print(red)
print(yellow)

# how to assign for the rest of the values in the tuple
x=("prince","aman","mohit","harshita","jyoti","garima")
(green,red,*yellow)=x
print(green)
print(red)
print(yellow)