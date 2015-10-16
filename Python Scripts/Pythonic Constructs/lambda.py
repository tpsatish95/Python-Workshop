# Using lambda
addTwo = lambda x: x+2
addTwo(2)
# 4

# the above is similar to
def addTwo(x):
    return x+2
addTwo(2)
# 4


# Use:
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(mult3)
# [3, 6, 9]

# Equivalent to
new = []
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if i % 3 == 0:
        new.append(i)
print(new)
# [3, 6, 9]
