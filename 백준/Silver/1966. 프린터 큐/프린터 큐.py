T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    que = [[val, idx] for idx, val in enumerate(map(int, input().split()))]
    count = 0

    while que:
        max_priority = max(que, key=lambda x: x[0])[0]  # 현재 큐에서 가장 높은 중요도 찾기
        cur_priority, cur_index = que.pop(0)  # 가장 앞의 문서 꺼내기

        if cur_priority < max_priority:  
            que.append((cur_priority, cur_index))
        else:
            count += 1
            if cur_index == M:
                print(count)
                break