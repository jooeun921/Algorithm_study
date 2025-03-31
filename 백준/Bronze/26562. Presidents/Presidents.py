from sys import stdin

money_dict = {
    'Franklin':100, 'Grant':50, 'Jackson':20, 'Hamilton':10, 'Lincoln':5, 'Washington':1
}

T = int(stdin.readline())
for _ in range(T):
    money = 0
    wallet = list(map(str, stdin.readline().split()))
    for paper in wallet:
        money += money_dict[paper]
    print(f"${money}")