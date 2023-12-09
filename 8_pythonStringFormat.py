# wrong method(don't do this)
# age=80
# txt="my age is "+age
# print(txt)

# method for concatenation
age=80
txt="my age is {}"
print(txt.format(age))


# format unlimited arguments
qty=8
itemno = 238
price=78.90
myorder="I want {} pieces of item number {} for price {} Rupees."
print(myorder.format(qty,itemno,price))


# format unlimited arguments with indexing
qty=8
itemno = 238
price=78.90
myorder="I want to pay{2} Rupees for {0} pieces of item number {1}."
print(myorder.format(qty,itemno,price))