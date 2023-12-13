# print each item of variable in list
print()
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

# looping through string
for i in "banana":
    print(i)


# the break statement
print()
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
    if i == "banana":
        break

# exit the loop when i is "banana" , but this time the break comes before print
print()
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        break
    print(i)
    if i == "banana":
        break


# continue statement

# the range() function
for i in range(6):
    print(i)  # 0 1 2 3 4 5

print()
# example of some deep range()
for i in range(2, 9):
    print(i)


print()
# you can specify value of increment by adding the 3rd parameter.
for i in range(4, 17, 3):
    print(i)


# Else in for loop
for i in range(6):
    print(i)
else:
    print("finally it finished")


# nested loops
adj = ["red", "big", "cherry"]
fruits = ["apple", "banana", "cherry"]
for i in adj:
    for j in fruits:
        print(i, "->", j)
