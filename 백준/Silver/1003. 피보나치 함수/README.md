# [Silver III] 피보나치 함수 - 1003 '⭐⭐'❣️'

문제 자체는 24416번을 풀고 나면 금방 풀 수 있었다. 다만, 이 0과 1의 호출횟수에 관해서 왜 n-1, n값인지는 생각해볼 여지가 있었기 때문에 물음표하트를 줬음.

[문제 링크](https://www.acmicpc.net/problem/1003)

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 3월 22일 18:40:05

### 문제 설명

<p>다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.</p>

<pre>int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
</pre>

<p><code>fibonacci(3)</code>을 호출하면 다음과 같은 일이 일어난다.</p>

<ul>
	<li><code>fibonacci(3)</code>은 <code>fibonacci(2)</code>와 <code>fibonacci(1)</code> (첫 번째 호출)을 호출한다.</li>
	<li><code>fibonacci(2)</code>는 <code>fibonacci(1)</code> (두 번째 호출)과 <code>fibonacci(0)</code>을 호출한다.</li>
	<li>두 번째 호출한 <code>fibonacci(1)</code>은 1을 출력하고 1을 리턴한다.</li>
	<li><code>fibonacci(0)</code>은 0을 출력하고, 0을 리턴한다.</li>
	<li><code>fibonacci(2)</code>는 <code>fibonacci(1)</code>과 <code>fibonacci(0)</code>의 결과를 얻고, 1을 리턴한다.</li>
	<li>첫 번째 호출한 <code>fibonacci(1)</code>은 1을 출력하고, 1을 리턴한다.</li>
	<li><code>fibonacci(3)</code>은 <code>fibonacci(2)</code>와 <code>fibonacci(1)</code>의 결과를 얻고, 2를 리턴한다.</li>
</ul>

<p>1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, <code>fibonacci(N)</code>을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다.</p>

<p>각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.</p>

### 출력

 <p>각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.</p>

### 메모

이전에 풀었던 브론즈의 24416번 피보나치 수 문제를 응용. 1이 호출되는 횟수는, 재귀형태로 n를 구할 때의 횟수와 동일함. 그리고 0은 n-1에 해당하는 횟수와 동일하고.
따라서 동적 프로그래밍(DP)을 활용하여 f(n) = f(n-1) +f(n-2)을 수행할 경우, 만들어지는 리스트(딕셔너리)는
{0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
다음의 형태를 띄게 됨.
