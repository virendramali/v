# Program to move all 0's at starting and
# remaining elements at last
a = [1, 0, 3, 3, 5, 0, 0, 4]
l = []
for i in a:
    if i == 0:
        l.insert(0, i)
    else:
        l.append(i)
print(l)
