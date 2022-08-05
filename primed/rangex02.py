#!/usr/bin/env python3

x = [1, 2, 3, 5]
i = 0
r = int(input("Enter upper range"))


def f(x): return x % 3 != 0 and x % 5 != 0
print(filter(f, range(2, r)))



