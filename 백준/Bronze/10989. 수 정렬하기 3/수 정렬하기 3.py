import sys 
N = int(sys.stdin.readline().rstrip())
dic = {}
for _ in range(N):
    X =int(sys.stdin.readline().rstrip())   
    if X in dic:
        dic[X] += 1
    else:
        dic[X] = 1
for i in range(max(dic.keys())+1):
    if i not in dic:
        continue
    else:
        for _ in range(dic[i]):
            print(i)