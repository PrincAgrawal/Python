# built-in data type

# text type : str
# numeric types : int,float,complex
# sequence type : list , tuple, range
# mapping : dict
# set type :  set,frozenset
# boolean type : bool
# Binary type : bytes, bytearray,memoryview

x=9
y="prince"
print(type(y))

x="prince agrawal"  #str
x=30 #int
x=40.009 # float
x=43j #complex
x=["sharad","khare"] #list
x=("sharad","khare") #tuple
x=range(5) #range
x={"name": "sharad","age":"100"} #dict
x={"apple","banana","orange"} #set
x=True #bool
x=b"sharad" #bytes
x=bytearray(5)  #bytearray
x=memoryview(bytes(5)) #memoryview




# setting out the spcific data type -->
x=str("sharad khare") 
x=int(20)
x= float(50.66)
x=complex(1j)
x= list(["prince","khare"])
x=tuple(("apple","banana"))
x=range(98)
x=dict(name="prince Agrawal",age=78)
x=set(("apple","banana"))
x=frozenset(("apple","sharad"))
x=bool(12)
x=bytes(5)
x=bytearray(6)
x=memoryview(bytes(7)) 
print(x)