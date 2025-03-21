from sys import stdin

N = int(stdin.readline().strip())
for i in range(N):
    sentence = stdin.readline().strip().split()
    print(f"Case #{i+1}:", *sentence[::-1])