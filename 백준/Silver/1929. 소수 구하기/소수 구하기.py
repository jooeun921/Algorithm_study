import sys
import math

m, n = map(int, sys.stdin.readline().strip().split())

def sieve(num):
    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False 

    for i in range(2, int(math.sqrt(num)) + 1):
        if is_prime[i]:
            for j in range(i * i, num + 1, i):
                is_prime[j] = False
    
    return is_prime
prime_table = sieve(n)

for num in range(m, n + 1):
    if prime_table[num]:
        print(num)