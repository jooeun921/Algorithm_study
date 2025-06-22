from collections import defaultdict

N = int(input())
name_list = defaultdict(int)

for _ in range(N):
    name = input()
    name_list[name[0]] += 1

ans = sorted([char for char, count in name_list.items() if count >= 5])

if not ans:
    print("PREDAJA")
else:
    print(''.join(ans))
