***암기 사항***
****pop() 과 insert()****
- pop()은 리스트에서 값을 꺼내면서 제거
    - pop():맨 마지막 값 꺼냄(pop(-1)과 같음
    - pop(i): i번쨰 인덱스 값 꺼냄
- insert()은 리스트에 값 삽입
    - insert(index,value) : index 위치에 value를 넣음
 
**rotate**
- rotate(n) : n칸 오른쪽(+) 또는 왼쪾으로(-)으로 회전

 # deque #
**매우 중요**
- deque: 양쪽 삽입/삭제가 빠른 리스트형 자료구조
- collections 모듈에서 import해서 사용해야 함.(from collections import deque)
    - dq = deque(list) 이렇게 -> 리스트를 deque로 변환
- deque 매서드
    - pop() : 오른쪽 끝 요소 제거 후 반환
    - popleft() : 왼쪽 첫 요소 제거 후 반환
    - append(x) : 오른쪽 끝에 x 추가
    - appendleft(x) : 왼쪽 맨 앞에 x 추
        
***2차원 배열에서 층과 열 구하기***
- 번호(num)주어 졌을 떄:</br>
- w : 한 층의 개수 제한</br>
> 1.층(row) = (num -1) // w </br>

- 2.열(index) 계산</br>
>방향이 지그재그 일때: (층마다 다르다고 생각해야함)
>
```
if row % 2 == 0:  # 짝수층이면 왼→오
    col = (num - 1) % w
else:             # 홀수층이면 오→왼
    col = (w - 1) - ((num - 1) % w)
```
정리 : 층마다 방향이 다를 때
| 계산 항목  | 공식                                                        |
| ------ | --------------------------------------------------------- |
| 층(row) | `(num - 1) // w`                                          |
| 열(col) | `짝수층: (num - 1) % w`<br> `홀수층: (w - 1) - ((num - 1) % w)` |


- 정렬 사용 (O(n log n))
    - 예시 : </br>
  ` def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])`
    - 정렬 : 리스트를 오름차순으로 정렬
    - 가능한 최대 곱:
        - 가장 큰 두수의 곱: `numbers[-1] * numbers[-2]`
        - 가장 작은 두 수의 곱 : `numbers[0] * numbers[1]`
- 부루트포스(모든 경우의 수를 전부 다 시도) (O(n²)임)
    - n< 1000 정도일 때 써도 됨
    - n >= 10000 이상 일땐 느려지니까 다른 방법 시도, 정렬, 그리디 등
