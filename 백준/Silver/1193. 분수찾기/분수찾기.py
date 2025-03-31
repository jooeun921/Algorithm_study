from sys import stdin

def 분수찾기(X):
    n = 1
    while X > n:
        X -= n
        n += 1
    
    if n % 2 == 0:
        분자 = X
        분모 = n - X + 1
    else:
        분자 = n - X + 1
        분모 = X
    
    return f"{분자}/{분모}"

X = int(stdin.readline())
print(분수찾기(X))
