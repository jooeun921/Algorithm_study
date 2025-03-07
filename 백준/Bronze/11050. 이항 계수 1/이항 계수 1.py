N, K = map(int, input().split())

def pac(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

if K == 0 or N == K:
    print(1)
else:
    print(int(pac(N) / (pac(K) * pac(N-K))))
