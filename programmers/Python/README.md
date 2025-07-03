# 알아 두어야 할 라이브러리 
import math -> 연산할 떄 사용가능
- 최대공약수를 활용해 최소 공배수 구하기(lcm 안먹힐 때)
- a * b // math.gcd(a, b)

| 함수/상수                 | 설명                                 |
| --------------------- | ---------------------------------- |
| `math.sqrt(x)`        | 제곱근 (√x)                           |
| `math.pow(x, y)`      | x의 y제곱 (실수 결과)                     |
| `math.factorial(n)`   | n! (팩토리얼)                          |
| `math.floor(x)`       | 내림 (소수점 아래 버림)                     |
| `math.ceil(x)`        | 올림                                 |
| `math.trunc(x)`       | 정수 부분만 잘라냄 (버림)                    |
| `math.fabs(x)`        | 절댓값 (실수 전용)                        |
| `math.gcd(a, b)`      | 최대공약수 (정수만 가능)                     |
| `math.lcm(a, b)`      | 최소공배수 (Python 3.9+)                |
| `math.log(x[, base])` | 로그 (기본은 자연로그 `ln(x)`, base로 변경 가능) |
| `math.log10(x)`       | 밑이 10인 로그                          |
| `math.log2(x)`        | 밑이 2인 로그                           |
| `math.exp(x)`         | e^x                                |
| `math.pi`             | 원주율 π (3.1415...)                  |
| `math.e`              | 자연상수 e (2.7182...)                 |
| `math.isqrt(n)`       | 정수 제곱근 (소수점 제거)                    |
| `math.isfinite(x)`    | 유한수인지 확인                           |
| `math.isnan(x)`       | NaN(Not a Number) 여부               |
| `math.copysign(x, y)` | x의 절댓값에 y의 부호를 붙인 값                |
| `math.hypot(x, y)`    | √(x² + y²) — 피타고라스 거리              |


import statistics

- 단일 숫자 목록(리스트, 튜플 등)을 받아서 평균,중앙값, 표준편차 등 다양한 통계값 계산 할떄 사용


| 함수                  | 설명                       |
| ------------------- | ------------------------ |
| `mean(data)`        | 산술 평균                    |
| `median(data)`      | 중앙값                      |
| `median_low(data)`  | 짝수 개일 때 더 작은 중앙값         |
| `median_high(data)` | 짝수 개일 때 더 큰 중앙값          |
| `mode(data)`        | 가장 자주 등장하는 값 (최빈값, 단 1개) |
| `multimode(data)`   | 최빈값이 여러 개일 경우 모두 리스트로 반환 |
| `stdev(data)`       | 표본의 표준편차                 |
| `pstdev(data)`      | 모집단의 표준편차                |
| `variance(data)`    | 표본의 분산                   |
| `pvariance(data)`   | 모집단의 분산                  |



import numpy as np <- np 거의 고정

- 중앙값, 평균, 최대 최소 등 숫자 데이터의 통계적 계산, 배열 기반 수치 연산 구할 떄 사용

| 함수                            | 설명                        |
| ----------------------------- | ------------------------- |
| `np.mean()`                   | 평균값                       |
| `np.median()`                 | 중앙값                       |
| `np.max()` / `np.min()`       | 최대값 / 최소값                 |
| `np.std()`                    | 표준편차 (standard deviation) |
| `np.var()`                    | 분산 (variance)             |

# 헷갈리는 문법 python
- for 문;
  - i in 배열:
    - 배열의 값 참조
  - i in range(len(배열)):
    - 인덱스와 순서 값 모두 참조 가능
- 

