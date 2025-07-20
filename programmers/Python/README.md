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
    - 대체 가능 함수 : enumerate
      - for i in enumerate(배열) 이렇게 쓰면 for i in ragne(len(배열)) 대체 가능  
  
- 슬라이싱

| 문법                  | 설명              |
| ------------------- | --------------- |
| `a[start:end]`      | start부터 end-1까지 |
| `a[:end]`           | 처음부터 end-1까지    |
| `a[start:]`         | start부터 끝까지     |
| `a[start:end:step]` | step 간격으로 추출    |
| `a[::-1]`           | 역순으로 전체 추출      |

- 리스트 컴프리헨션
  - [표현식 for 변수 in 반복가능한객체 if 조건]
    - [x**2 for x in range(10) if x % 2 == 0]
    - 만약 표현식에 두개의 인자를 받고 싶으면 ()나 []로 감싸줘야 함. 아니면 에러남 만약 근데 만약 이렇게 리턴하면 리스트안에 튜플, 리스트로 반환 되기 떄문에 값을 두개 반환 하고 싶으면 다르게 표현을 해야함 따로 변수를 지정한다든지
- 딕셔너리 컴프리헨션
  - {key: value for 변수 in 반복가능한객체}
  - {x: x**2 for x in range(1, 6) if x % 2 == 0}
  - d = {char: idx for idx, char in enumerate(s)}
- 람다식 : 이름 없는 간단한 함수를 한 줄로 정의하는 방법
  - lambda 매개변수: 표현식
    - add = lambda x, y: x + y
    - print(add(3, 5))  # → 8  
  - map() 과 filter()와 함께 사용됨
    - map() : 모든 원소에 함수를 적용한 결과를 반환
      - map(lambda x: x**2, nums) -> 이런식으로 활용
    - filter() : 함수 조건을 통과하는 원소만 걸러냄
      - filter(lambda x: x % 2 == 0, nums)
  - sorted() + key : 리스트 등을 정렬할 때 사용하는 함수
    - sorted(리스트, key=정렬기준함수(생략가능), reverse=True/False(생략가능 생략하면 오름차순)) -> 내림차순 하고 싶을 땐 True
    - sorted(words, key=lambda x: len(x))
    - list.sort() 이렇게 사용할 수도 있음 -> 오름차순 정렬
- 튜플 : 각 값에 대응하는 값을 리턴하고 싶을 때 간편하게 사용할 수 있음
- 딕셔너리 : Key:Value (키:값) 쌍으로 데이터를 저장하는 자료형
  - d = {}
  - d['a'] = 1
  - d['b'] = 2
  - 이렇게 쓰거나
  - d = dict(a=1, b=2) 이렇게 써도 됨

# Python 내장 함수
- min() : 최솟값
- sum() : 합
- max() : 최댓값
- count() : 특정 값 몇번 등장하는지 반환
  - 문자열(str) 사용가능
  - 리스트 사용 가능
  - 튜플 사용 가능
  - *숫자 사용 안됨*
    - text.count('찾고싶은 것') 이렇게 씀
    - 숫자를 세고 싶으면 문자열로 변환해서 쓰면 구해지긴 함
      - str(n).count(str(k))이렇게 n,k둘다 정수 일 때
- map() : 반복 가능한 값들에 함수를 하나하나 적용해서 새로운 값으로 바꿔주는 도구 (보통 list()나 sum() 같은 걸로 감싸서 씀)
  - map(함수, 반복가능한_자료) 
  - list(map(int, str_nums)) (str_nums는 문자열 리스트)
- upper() : 모두 대문자로 변환
- lower() : 모두 소문자로 변환
- capitalize() : 맨 앞 글자만 대문자, 나머지는 소문자
- title() : 단어마다 맨 앞 글자 대문자
- swapcase() : 대소문자 서로 변환
- isupper() : 대문자인지 판별
- islower() : 소문자인지 판별
- isalpha() : 모든 문자가 알파벳인지 확인
- isdigit() : 모든 문자가 숫자인지 확인
- isalnum() : 모든 문자가 알파벳 또는 숫자인지 확인
- isspace() : 모든 문자가 공백인지 확인
- .index(value) : 리스트에서 해당 값이 처음 등장한 위치 반환
- .rindex(value) : 뒤에서부터 찾음
- ''.join(리스트) : 리스트 값을 문자열로 합칠 때 사용 '','-','/' 등 사용 가능

# 헷갈리는 사항
- 문자열은 불변
  - 수정불가능 -> 수정하려면 일단 리스트로 변환 해야함
  - 값 변경 불가능 -> 변경 하고 싶으면 리스트로 변경 해야
  - 인덱싱은 가능
  - 슬라이싱 가능
