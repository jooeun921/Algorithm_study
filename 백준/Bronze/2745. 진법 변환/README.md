# [Bronze II] 진법 변환 - 2745 '⭐'❣️'

[문제 링크](https://www.acmicpc.net/problem/2745)

### 성능 요약

메모리: 32544 KB, 시간: 36 ms

### 분류

구현, 문자열, 수학

### 제출 일자

2025년 3월 20일 21:00:51

### 문제 설명

<p>B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.</p>

<p>10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.</p>

<p>A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35</p>

### 입력

 <p>첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)</p>

<p>B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.</p>

### 출력

 <p>첫째 줄에 B진법 수 N을 10진법으로 출력한다.</p>

### 메모

나의 패착...ㅠㅠ 아니 원래도 진법 변환할 때 이 방식(알파벳)으로 쓰는 줄 몰랐다...
물론 파이썬 함수 int()에서 진법 변환을 지원하는 줄도 몰랐지만;;

n진수 → 10진수

- 결과값은 모두 string 입니다.
  int(string, base) -> string은 변환하고자 하는 n진수 숫자 값. base는 n에 해당하는 진수값.
