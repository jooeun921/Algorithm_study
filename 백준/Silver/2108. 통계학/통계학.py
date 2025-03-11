import sys
from collections import Counter

N = int(input())
if N == 1:
    num = int(input())
    print(num, num, num, 0, sep='\n')
else:
    num_list = list(int(sys.stdin.readline().strip()) for _ in range(N))

    # 산술평균
    print(round(sum(num_list)/N))

    # 중앙값
    num_list.sort()
    print(num_list[N//2])

    # 최빈값. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
    counter = Counter(num_list)
    counter_list = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    print(counter_list[1][0] if (len(counter_list) > 1 and counter_list[0][1]==counter_list[1][1]) else counter_list[0][0])

    # 범위
    print(num_list[-1] - num_list[0])