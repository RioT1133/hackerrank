a = input().split()

x1 = int(a[0].strip())
v1 = int(a[1].strip())
x2 = int(a[2].strip())
v2 = int(a[3].strip())

d1 = abs(x1 - x2)
d2 = abs((x1 + v1) - (x2 + v2))

if d2 >= d1:
    print("NO")
elif d1%(d2-d1) == 0:
    print("YES")
else:
    print("NO")