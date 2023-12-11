x=1
y=5.9
z=1j
print(type(x))
print(type(y))
print(type(z))

# int numeric type
x=1
y=437847874724
z=-74568
print(type(x))
print(type(y))
print(type(z))

# floator floating point number data type
x=1.9870
y=437847874724.00
z=-74568.65
print(type(x))
print(type(y))
print(type(z))

# float can also be scientific numbers with an "e"

x=35e79
print(type(x))

# complex numbers are written with a j asthe imaginary part
x=3+5j
y=6j
z=-8j
print(x+y+z)


# type conversion
x=4
y=7.9
z=1j

a=float(x)
print(a)
b=int(y)
print(b)
c=complex(y)
print(c) 


# random number
import random
print(random.randrange(1,7))