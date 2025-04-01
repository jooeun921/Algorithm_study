from sys import stdin

K = int(stdin.readline())

for i in range(1, K + 1):
    n, M = map(float, stdin.readline().split())
    stages = []

    for _ in range(int(n)):
        mi, ti, Fi = map(float, stdin.readline().split())
        stages.append((mi, ti, Fi))

    h = 0.0
    v = 0.0
    total_mass = M + sum(mi for mi, _, _ in stages)

    for mi, ti, Fi in stages:
        a = (Fi / total_mass) - 9.81
        h += v * ti + 0.5 * a * ti**2
        v += a * ti
        total_mass -= mi

    print(f"Data Set {i}:")
    print(f"{h:.2f}")
    print()
