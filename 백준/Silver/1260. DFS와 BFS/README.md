# [Silver II] DFS와 BFS - 1260 '⭐⭐⭐⭐'❣️'

[문제 링크](https://www.acmicpc.net/problem/1260)

### 성능 요약

메모리: 35608 KB, 시간: 68 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2025년 4월 3일 20:49:28

### 문제 설명

<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.</p>

### 입력

 <p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.</p>

### 출력

 <p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</p>

### 메모

깊이우선탐색(DFS)와 너비우선탐색(BFS)의 개념과 구현 방법을 알면 풀 수 있다!
깊이우선탐색은 재귀 or stack을 활용하여 구현할 수 있다. 단 stack의 경우에는 extend와 reversed 활용하여 그 위치의 인덱스 값을 뒤집어서 전부 넣는다.
너비우선탐색은 deque를 활용하여 구현할 수 있다. 해당 리스트 내의 값을 전부 넣는다.

처음 주어진 값을 가지고 graph를 만들 때

1. 간선에 따라 양방향 간선, 단방향 간선
2. dictionary, 2차원 list 모두 가능함!

```
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]

1. 딕셔너리
graph = {}  # 빈 딕셔너리 생성

for a, b in edges: # 처음에 key가 없을 수도 있기 때문에 -> 없는 경우에 key를 a로 하고 그 뒤에 value b를 넣어준다.
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

# 노드별 인접 리스트 정렬 (필요하면)
for key in graph:
    graph[key].sort()  # 정렬해서 탐색 순서 일정하게게

2. 리스트
graph = [[] for _ in range(N+1)] # 빈 2차원 리스트 만들기
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
graph = list(map(sorted, graph))
```
