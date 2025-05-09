# [Silver I] 단지번호붙이기 - 2667 '⭐⭐⭐'

[문제 링크](https://www.acmicpc.net/problem/2667) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 3일 21:28:54

### 문제 설명

<p><그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="" style="height:192px; width:409px"></p>

### 입력 

 <p>첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.</p>

### 출력 

 <p>첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.</p>

### 메모

- **문제 핵심**:
  - 주어진 N×N 크기의 지도에서 1로 연결된 단지를 탐색하고, 각 단지의 크기를 구하는 문제입니다.
  - 단지는 상하좌우로 연결된 1의 집합으로 정의됩니다.

---

- **알고리즘**:
  1. **DFS 탐색**:
     - 각 단지의 시작점을 발견하면 DFS를 통해 연결된 모든 1을 탐색합니다.
     - 탐색된 1은 방문 처리(0으로 변경)하여 중복 탐색을 방지합니다.
     - 단지의 크기를 카운트합니다.
  2. **단지 크기 저장**:
     - 탐색이 끝날 때마다 단지의 크기를 리스트에 저장합니다.
  3. **결과 출력**:
     - 단지의 개수와 각 단지의 크기를 오름차순으로 출력합니다.

---

- **시간 복잡도**:
  - 전체 격자를 한 번씩 방문하므로 시간 복잡도는 **O(N²)**입니다.
  - DFS의 탐색 깊이는 단지의 크기에 비례하므로, 최악의 경우에도 **O(N²)**입니다.

---

- **주의사항**:
  1. 입력으로 주어진 지도는 반드시 정수로 변환하여 처리해야 합니다.
  2. 방문한 위치는 반드시 0으로 변경하여 중복 탐색을 방지합니다.
  3. 단지 크기를 저장한 리스트는 오름차순으로 정렬하여 출력해야 합니다.

---

- **코드 설명**:
  - `dfs(x, y)`:
    - 스택을 사용하여 DFS를 구현합니다.
    - 현재 위치에서 상하좌우로 이동하며 연결된 1을 탐색합니다.
  - `complex_list`:
    - 각 단지의 크기를 저장하는 리스트입니다.
  - `complex_list.sort()`:
    - 단지 크기를 오름차순으로 정렬합니다.