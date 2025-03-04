n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
print('\n'.join(' '.join(map(str, C[i])) for i in range(n)))