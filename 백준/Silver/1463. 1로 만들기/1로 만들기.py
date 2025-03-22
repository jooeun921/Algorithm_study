def make_one(n):
    num_list = [0] * (n + 1)
    for i in range(2, n + 1):
        num_list[i] = num_list[i - 1] + 1 # 기본 연산. 이전꺼에서+1 한 개 dp 연산 횟수니까.
        if i % 2 == 0:
            num_list[i] = min(num_list[i], num_list[i // 2] + 1) # dp[i]는 1만 더하는 연산
        if i % 3 == 0:
            num_list[i] = min(num_list[i], num_list[i // 3] + 1)
    return num_list[n]

n = int(input())  
print(make_one(n))