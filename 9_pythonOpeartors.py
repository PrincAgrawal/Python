# Arithmatic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# membership Operators
# Bitwise Operators


# 1. Arithmatic Opeartors -->
x=10
y=5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)


# 2. Assignment Opeartors

# x=x+3 same as x+=3
# x=x-3 same as x-=3
# x=x*3 same as x*=3
# x=x/3 same as x/=3
# x=x%3 same as x%=3
# x=x**5 same as x**=5
x=5
x%=3
print(x)


# Comparison Opeartor

x=8
y=9
print(x<=y)
print(x==y)
print(x>=y)
print(x>y)
print(x<y)
print(x!=y)


# Logical opeartor

x=8
print(x>3 and x<10)
print(x<3 or x>5)
print(not(x>3 and x<10))


# Identity Operator
x=["prince","Agrawal"]
y=["prince","Agrawal"]
z=x
print(x is z)  # return true because z is the same object as x.
print(x is y)  #object same
print(x==y)  #values same



# membership operator
x=["banana","apple","payaya","laddu"]
print("banana" in x)

print("banana" not in x)