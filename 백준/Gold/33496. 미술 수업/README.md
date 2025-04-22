# [Gold IV] 미술 수업 - 33496 

[문제 링크](https://www.acmicpc.net/problem/33496) 

### 성능 요약

메모리: 141024 KB, 시간: 796 ms

### 분류

이분 탐색, 자료 구조, 기하학, 해시를 사용한 집합과 맵, 수학, 스위핑

### 제출 일자

2025년 3월 28일 22:28:42

### 문제 설명

<p>창하는 재작년 미술 수업 최종 프로젝트로 다음과 같은 그림을 그린 덕분에 과목우수상을 받았다.</p>

<ol>
	<li>비어있는 2차원 좌표평면을 준비한다.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 점 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.024em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.024em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.024em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><msub><mi>X</mi><mn>1</mn></msub><mo>,</mo><msub><mi>Y</mi><mn>1</mn></msub><mo stretchy="false">)</mo><mo>,</mo><mo stretchy="false">(</mo><msub><mi>X</mi><mn>2</mn></msub><mo>,</mo><msub><mi>Y</mi><mn>2</mn></msub><mo stretchy="false">)</mo><mo>,</mo><mo>⋯</mo><mo>,</mo><mo stretchy="false">(</mo><msub><mi>X</mi><mi>N</mi></msub><mo>,</mo><msub><mi>Y</mi><mi>N</mi></msub><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(X_1, Y_1), (X_2, Y_2), \cdots, (X_N, Y_N)$</span></mjx-container>을 정한다. 단, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3E"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Y</mi><mi>i</mi></msub><mo>></mo><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Y_i > 0$</span></mjx-container>이다.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>축을 나타내는 직선을 그린다.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>⋯</mo><mo>,</mo><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i = 1, 2, \cdots, N$</span></mjx-container>에 대해 점 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.024em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><msub><mi>X</mi><mi>i</mi></msub><mo>,</mo><msub><mi>Y</mi><mi>i</mi></msub><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(X_i, Y_i)$</span></mjx-container>을 지나고, 기울기가 각각 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>과 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-1$</span></mjx-container>인 두 개의 직선을 그린다. 단, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>축 아래의 부분은 그리지 않는다.</li>
</ol>

<p>아래는 창하의 그림의 예시를 나타낸 것이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b8a0c69c-2b49-4102-a6c3-a6df1ee4fb95/-/preview/" style="height: 264px; width: 450px;"></p>

<p>과목우수상의 비결은 그림에 등장하는 교점의 아름다운 조화라고 생각한 에릭은 창하의 그림에 등장하는 서로 다른 교점의 개수를 구해보고자 한다. 이때 완전히 겹치는 직선들은 하나의 직선으로 취급한다.</p>

### 입력 

 <p>첫 번째 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>다음 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄 중 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 줄에 두 개의 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.024em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$X_i$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Y</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Y_i$</span></mjx-container>가 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>창하의 그림에 등장하는 서로 다른 교점의 개수를 출력한다.</p>

### 메모

- **문제 핵심**: 
  - 주어진 점들로부터 두 종류의 대각선을 정의하고, 이 대각선들이 교차하는 지점(교점)의 개수를 계산하는 문제입니다.
  - 대각선은 점의 좌표를 이용해 두 가지 방식으로 정의됩니다:
    1. `diag_plus`: 각 점의 `(x - y)` 값을 기준으로 대각선을 정의.
    2. `diag_minus`: 각 점의 `(x + y)` 값을 기준으로 대각선을 정의.

---

- **대각선 정의**:
  - `diag_plus`: 점 `(x, y)`에서 `(x - y)` 값을 계산하여 대각선을 정의합니다. 이 값이 같으면 같은 대각선에 속합니다.
    - 예: 점 `(3, 2)`의 `diag_plus` 값은 `3 - 2 = 1`입니다.
  - `diag_minus`: 점 `(x, y)`에서 `(x + y)` 값을 계산하여 대각선을 정의합니다. 이 값이 같으면 같은 대각선에 속합니다.
    - 예: 점 `(3, 2)`의 `diag_minus` 값은 `3 + 2 = 5`입니다.

---

- **교집합과 합집합**:
  - `meet`: `diag_plus`와 `diag_minus`의 교집합으로, 두 대각선이 겹치는 경우를 나타냅니다.
    - 예: 어떤 대각선이 `diag_plus`와 `diag_minus` 모두에 속하면 교집합에 포함됩니다.
  - `example`: `diag_plus`와 `diag_minus`의 합집합에서 교집합을 제외한 부분입니다.
    - 예: `diag_plus` 또는 `diag_minus` 중 하나에만 속하는 대각선.

---

- **정렬 및 계산**:
  - `diag_plus`와 `diag_minus`를 정렬하여 대각선 간의 관계를 효율적으로 계산합니다.
  - 정렬된 두 리스트를 투 포인터 방식으로 비교하며, 특정 조건을 만족하는 대각선의 개수를 계산합니다.
    - 투 포인터 방식: 두 리스트를 동시에 순회하며, 조건에 따라 포인터를 이동시켜 계산을 최적화합니다.

---

- **알고리즘 과정**:
  1. 입력으로 주어진 점들로부터 `diag_plus`와 `diag_minus`를 생성합니다.
  2. `diag_plus`와 `diag_minus`를 각각 정렬합니다.
  3. 두 정렬된 리스트를 투 포인터 방식으로 순회하며, 교점의 개수를 계산합니다:
     - `diag_plus[i] < diag_minus[j]`인 경우, `diag_plus[i]`보다 큰 `diag_minus`의 개수를 계산하고 포인터를 이동합니다.
     - 그렇지 않으면 `diag_minus`의 포인터를 이동합니다.
  4. 최종적으로 `cnt`(교점 개수), `meet`(교집합 크기), `example`(합집합에서 교집합 제외 크기)의 합을 출력합니다.

---

- **시간 복잡도**:
  - 대각선 집합 생성: O(N) (점의 개수만큼 반복)
  - 정렬: O(K log K) (K는 대각선의 개수)
  - 투 포인터 계산: O(K)
  - 전체 시간 복잡도는 O(N + K log K)로, N이 크더라도 효율적으로 처리 가능합니다.

---

- **결과**:
  - 최종 출력은 `cnt`(조건을 만족하는 대각선의 개수)와 `meet`, `example`의 크기를 합산한 값입니다.

---

- **주의사항**:
  1. 입력 점의 개수(N)가 크더라도, 대각선 집합의 크기(K)는 상대적으로 작을 수 있습니다.
  2. 투 포인터 방식은 정렬된 리스트에서만 사용할 수 있으므로, 정렬이 필수입니다.
  3. 중복된 대각선은 하나로 취급해야 하므로, 집합(set)을 사용하여 중복을 제거합니다.