n = int(input())
a = input().split()

diff = []
counts = []

longest = 1
for i in a:
    if int(i) not in diff:
        diff.append(int(i))

for i in diff:
    count = 0
    for j in a:
        if int(j) == i:
            count += 1
    counts.append(count)

for i in range(len(diff)-1):
    for j in range(i+1, len(diff)):
        if abs(diff[i] - diff[j]) <= 1:
            if counts[i] + counts[j] > longest:
                longest = counts[i] + counts[j]

for i in range(len(counts)):
    if counts[i] > longest:
        longest = counts[i]
        
print(longest)
