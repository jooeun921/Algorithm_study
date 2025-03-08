import sys
readline = sys.stdin.readline
output = sys.stdout

N = int(readline().strip())
persons = [list(map(str, readline().split())) for i in range(N)]
p_new = sorted(persons, key= lambda x: int(x[0]))

for person in p_new:
    print(" ".join(person))