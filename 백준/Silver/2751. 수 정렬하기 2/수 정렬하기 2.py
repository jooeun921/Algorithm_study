import sys
N = int(sys.stdin.readline().strip())
num_list = []
for i in range(N):
    a = int(sys.stdin.readline().strip())
    num_list.append(a)
num_list.sort()
print(*num_list, sep='\n')