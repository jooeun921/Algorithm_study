import sys
N = int(sys.stdin.readline().strip())
eng = set()
for _ in range(N):
    eng.add(sys.stdin.readline().strip())
eng_li = sorted(eng, key=lambda x: (len(x), x))
print(*eng_li, sep='\n')