# python has 2 primitive loops
# 1. while loop
# 2. for loop

# the while loop
i = 1
while i <= 6:
    print(i)
    i += 1

print()
# the braek statement ->
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

print()
# the continue statement
i = 1
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)


# the else statement
i = 1
while i < 9:
    print(i)
    i += 1
else:
    print("i is no longer less than ", i)
