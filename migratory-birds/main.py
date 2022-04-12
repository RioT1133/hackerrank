import math
n = int(input())
a = input().split()

arr = []
different_counts = {}

for i in a:
    arr.append(int(i))

for i in arr: # make a dictionary for different birds and their counts
    if i not in different_counts.keys():
        different_counts[i] = 1
    else:
        different_counts[i] += 1

most_birds = max(different_counts.values())
birds_with_most_birds = []

for i in different_counts:
    if different_counts[i] == most_birds:
        birds_with_most_birds.append(i)

print(min(birds_with_most_birds))