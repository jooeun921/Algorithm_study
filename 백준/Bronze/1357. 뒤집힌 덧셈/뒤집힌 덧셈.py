def Rev(x: str):
    x_rev = x[::-1]
    return int(x_rev)

x, y = map(str, input().split())

print(Rev(str(Rev(x) + Rev(y))))