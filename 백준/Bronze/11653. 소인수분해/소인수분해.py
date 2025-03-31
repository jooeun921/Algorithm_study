from sys import stdin
import math

def get_prime(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return [x for x in range(2, n + 1) if prime[x]]

def factorize(N):
    primes = get_prime(N)

    for prime in primes:
        while N % prime == 0:
            print(prime)
            N //= prime

    if N > 1:
        print(N)

N = int(stdin.readline().strip())

if N != 1:
    factorize(N)
