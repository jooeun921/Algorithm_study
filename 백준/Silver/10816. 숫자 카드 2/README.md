# [Silver IV] 숫자 카드 2 - 10816

[문제 링크](https://www.acmicpc.net/problem/10816)

### 성능 요약

메모리: 141172 KB, 시간: 524 ms

### 분류

이분 탐색, 자료 구조, 해시를 사용한 집합과 맵, 정렬

### 제출 일자

2025년 3월 10일 19:49:45

### 문제 설명

<p>숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.</p>

<p>셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.</p>

### 출력

 <p>첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.</p>

### 메모

그냥 반복문 돌려서 출력하는 걸로 하려고 했는데 시간초과가 뜸.
-> 딕셔너리로 만들어서 딕셔너리에 key가 없으면 value 1로 해서 추가. 있으면 += 로 value 추가.
그리고 마지막에 get으로 m_list에 있는 m이 n을 가지고 만든 딕셔너리에 있으면 get으로 value 가져오고 없으면 0으로 출력. join은 문자열 리스트만 받기 때문에 str 변환도 해줘야 함.
