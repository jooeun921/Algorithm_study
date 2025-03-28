from sys import stdin

N = int(stdin.readline())
N_list = [list(map(int, stdin.readline().split())) for _ in range(N)]

diag_plus = set(x - y for x, y in N_list)
diag_minus = set(x + y for x, y in N_list)

# meet은 교집합, example은 합집합에서 교집합을 뺀 부분
meet = diag_plus & diag_minus
example = (diag_plus | diag_minus) - meet

# diag_plus와 diag_minus를 정렬
diag_plus = sorted(diag_plus)
diag_minus = sorted(diag_minus)

# cnt 계산
cnt = 0
i, j = 0, 0
while i < len(diag_plus) and j < len(diag_minus):
    if diag_plus[i] < diag_minus[j]:
        cnt += len(diag_minus) - j  # diag_plus[i]보다 큰 diag_minus의 개수
        i += 1
    else:
        j += 1

# 최종 출력
print(cnt + len(meet) + len(example))
