#!/usr/bin/env python3

x = []
i = 49

while i > 0:
    i = i - 1
    if i%2 != 0 and i%3 != 0 and i%5 !=0:
        x.append(i)
x.append(5)
x.append(3)
x.append(2)


print(x)

