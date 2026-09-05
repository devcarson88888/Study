#!/usr/bin/env/python3/
#题号:P1035
#PyPy3 or cpython3
n = int(input())
ans = 0.0
i = 1
while ans <= n:
    ans += 1.0 / i
    i += 1
print(i - 1)
