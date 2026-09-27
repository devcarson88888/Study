import sys

a, b, c, d = map(float, sys.stdin.readline().split())

def f(x):
    return ((a * x + b) * x + c) * x + d
  
roots = []

for i in range(-10000, 10000):
    left = i / 100
    right = (i + 1) / 100

    fl = f(left)
    fr = f(right)

    if fl * fr <= 0:
        l, r = left, right
      
        for _ in range(60):
            mid = (l + r) / 2
            fm = f(mid)

            if fl * fm <= 0:
                r = mid
            else:
                l = mid
                fl = fm

        root = (l + r) / 2

        if not roots or root - roots[-1] > 0.5:
            roots.append(root)

print(*[f"{root:.2f}" for root in roots])
