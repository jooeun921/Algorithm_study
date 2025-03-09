import sys
readline = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, readline().strip().split())
f_list = [readline().strip() for _ in range(N)]
min_count = float('inf')

for i in range(N-7):
    for j in range(M-7):
        count_B = 0
        count_W = 0

        for x in range(8):
            for y in range(8):
                expected_B = 'B' if (x+y) % 2 == 0 else 'W'
                expected_W = 'W' if (x+y) % 2 == 0 else 'B'

                if f_list[i+x][j+y] != expected_B:
                    count_B += 1
                if f_list[i+x][j+y] != expected_W:
                    count_W += 1
        min_count = min(min_count, count_B, count_W)

write(str(min_count))