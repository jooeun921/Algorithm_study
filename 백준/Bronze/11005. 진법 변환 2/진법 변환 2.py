# N_list = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}


# N, B = map(int, input().split())
# ans = ''
# while N > 0:
#     N, mod = divmod(N, B)
#     if mod >= 10:
#         ans += N_list[mod]
#     else:
#         ans += str(mod)

# print(ans[::-1])


# 더 간단한 풀이. 어차피 나머지를 가지고 계산하므로, 나머지마다 문자열에 더해주면 됨. 다음 계산에 필요한 값은 몫을 활용해서 재할당
n,b=map(int,input().split())

number='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=''
while n:
    s+=str(number[n%b])
    n//=b

print(s[::-1])