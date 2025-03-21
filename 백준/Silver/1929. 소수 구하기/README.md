# [Silver III] 소수 구하기 - 1929 '⭐⭐⭐⭐⭐'

[문제 링크](https://www.acmicpc.net/problem/1929)

### 성능 요약

메모리: 42212 KB, 시간: 208 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2025년 3월 11일 21:26:32

### 문제 설명

<p>M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.</p>

### 출력

 <p>한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.</p>

### 메모

에라토스테네스의 체 : 소수를 찾는 가장 빠르고 쉬운 방법.

1. 구하고자 하는 구간을 설정.
2. 2부터 2를 제외한 2의 배수를 제거한다.
3. 그 다음 가장 작은 수인 3부터 3을 제외한 3의 배수 제거.
   ... 반복한다!
   이때, 반복은 구하고자 하는 제곱수 이전까지만 수행하면 되는데, 곱셈 연산은 반복되기 때문이다!

여기에서 i*i부터 시작하는 것은 그보다 작은 수들은 앞에서 이미 걸러졌기 때문! ex. i = 2이면, 4부터 step=2 2칸씩 점프해서 false로 지워버림.
for j in range(i * i, num + 1, i):
is_prime[j] = False

최종적으로 내가 구하고자 하는 m부터 n까지 true와 false로 구성된 소수 찾기 리스트를 함수로 만들고, 구간을 돌면서 true일 때의 num을 출력하면 된다.
