P, K = map(int, input().split())

def is_prime(P, K):
    prime = [True] * K
    prime[0] = prime[1] = False
    for i in range(2, int(K**0.5) + 1):
        if prime[i]:
            for j in range(i*i, K, i):
                prime[j] = False

    for i in range(2, K):
        if prime[i]:
            if P % i == 0:
                print(f"BAD {i}")
                return
    print("GOOD")

is_prime(P, K)