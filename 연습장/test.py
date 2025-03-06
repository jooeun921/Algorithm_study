# r의 값은 26보다 큰 소수인 31로 하고 M의 값은 1234567891
# 항의 번호에 해당하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 더하는 것

# 알파벳 순서대로 그거의 거듭제곱으로 곱해줌.
# 문자열이 abcd라고 하면,
# a(1)는 r의 1 제곱. b(2)는 r의 제곱, c(3)는 r의 세제곱, d(4)는 r의 네제곱으로 계산하게 됨. 그것의 전체 sum / M -> 정수로 출력.

from string import ascii_lowercase
aList = list(ascii_lowercase)

L = int(input())
a_list = input()
ans = 0

for i in range(L):
    ans += (aList.index(a_list[i]) + 1) * (31 ** i)
print(ans % 1234567891)