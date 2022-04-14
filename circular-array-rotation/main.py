nkq = input().split()
nkq = [int(i) for i in nkq]
a = input().split()
a = [int(i) for i in a]
queries = []

n = nkq[0]
k = nkq[1]
q = nkq[2]

k = k % n

for i in range(q): # getting all the queries
    element = int(input())
    queries.append(element)

def rotate_array(_a, _n): # rotates array a n times (surely there's a way to do it without loops)
    r = [_a[-i] for i in range(_n, 0, -1)]
    for i in range(0, len(_a) -len(r)):
        r.append(a[i])
    return r

rotated = rotate_array(a, k)

for i in range(q):
    print(rotated[queries[i]])