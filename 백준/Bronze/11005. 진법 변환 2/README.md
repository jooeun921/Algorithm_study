# [Bronze I] 진법 변환 2 - 11005 '⭐⭐❣️'

[문제 링크](https://www.acmicpc.net/problem/11005)

### 성능 요약

메모리: 32544 KB, 시간: 40 ms

### 분류

구현, 수학

### 제출 일자

2025년 3월 20일 23:49:54

### 문제 설명

<p>10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.</p>

<p>10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.</p>

<p>A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35</p>

### 입력

 <p>첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.</p>

### 출력

 <p>첫째 줄에 10진법 수 N을 B진법으로 출력한다.</p>

### 메모

divmod를 알면 좀 더 쉽게 정리할 수 있음! divmod는 몫과 나머지를 튜플로 반환해주는 내장 함수임.
B진법으로 출력하려면 B진법의 나머지 순서대로 입력하고, 그걸 거꾸로 출력하면 됨.

- 예를 들어서 7을 2진법으로 변환하려면, 먼저 7을 2로 나눈다. 몫과 나머지가 3과 1이 나옴.
  '1' 입력.
  몫 3을 2로 나눔. 몫과 나머지가 1, 1.
  나머지 1 넣기.
  몫 1을 2로 나눔. 몫 0, 나머지 1.
  나머지합 = 111
  -> 이거 뒤집어야 답.

근데 굳이 이거 몰라도 되더라.
