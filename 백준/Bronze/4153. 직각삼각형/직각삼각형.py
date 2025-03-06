while True:
    li = list(map(int, input().split()))
    if all(val == 0 for val in li):
        break

    li_sort = li.sort()

    if (li[-1])**2 == (li[0]) ** 2 + (li[1]) ** 2:
        print("right")
    else:
        print("wrong")