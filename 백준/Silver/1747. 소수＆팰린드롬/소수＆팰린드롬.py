import math

def 소수(size):
    소수_list = [True] * (size + 1)
    소수_list[0] = 소수_list[1] = False
    for i in range(2, int(math.sqrt(size)) + 1):
        if 소수_list[i]:
            for j in range(i * i, size + 1, i):
                소수_list[j] = False
    return 소수_list

def 팰린드롭(x):
    x_str = str(x)
    return x_str == x_str[::-1]

def 가장_작은_소수_팰린드롬(N, size):
    소수_list = 소수(size)
    for i in range(N, size + 1):
        if 소수_list[i] and 팰린드롭(i):
            return i

N = int(input())
size = 10000000

print(가장_작은_소수_팰린드롬(N, size))
