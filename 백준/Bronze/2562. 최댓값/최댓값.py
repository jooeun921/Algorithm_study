import sys
li = []
max = 0
for i in range(9):
    li.append(int(sys.stdin.readline()))
    if max < li[i]:
        max = li[i]
print(max, li.index(max)+1, sep='\n')