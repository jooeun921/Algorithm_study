li = list(range(1, 31, 1))
for _ in range(28):
    a = int(input())
    li.remove(a)
print(*li, sep="\n")