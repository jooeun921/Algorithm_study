# N = int(input())
# R, C = map(int, input().split())

# if N == 3:
#     if R == 2 and C == 2:
#         print(1)
#     else:
#         print(4)
# else:
#     print((N**2 + 1)//2 if (R+C)%2==0 else (N**2)//2)

# 조금 더 단축한 버전
N = int(input())
R, C = map(int, input().split())

if (N, R, C) == (3, 2, 2):
    print(1)
else:
    print((N**2 + 1)//2 if (R+C)%2==0 else (N**2)//2)