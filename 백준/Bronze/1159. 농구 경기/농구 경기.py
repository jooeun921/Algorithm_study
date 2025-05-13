from sys import stdin
from collections import defaultdict

n = int(stdin.readline())

name_dict = defaultdict(int)

for _ in range(n):
    name = stdin.readline()
    first_letter = name[0]
    name_dict[first_letter] += 1

result = [i for i in sorted(name_dict) if name_dict[i] >= 5]

if result:
    print(*result, sep='')
else:
    print("PREDAJA")
