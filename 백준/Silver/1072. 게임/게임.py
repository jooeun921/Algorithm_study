from sys import stdin

def min_games_needed(x, y):
    z = (y * 100) // x

    if z >= 99:
        return -1

    left, right = 1, x
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        new_z = ((y + mid) * 100) // (x + mid)

        if new_z > z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

x, y = map(int, stdin.readline().split())
print(min_games_needed(x, y))