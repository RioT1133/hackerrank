nkq = input().split()
nkq = [int(i) for i in nkq]
a = input().split()
a = [int(i) for i in a]
queries = []

n = nkq[0]
k = nkq[1]
q = nkq[2]

for i in range(n): # getting all the queries
    element = int(input())
    queries.append(element)

def rotate_array(a, n): # rotates array a n times (surely there's a way to do it without loops)
    r = [a[-i] for i in range(1, n+1)]
    for i in a[:-n]:
        r.append(i)
    return r

