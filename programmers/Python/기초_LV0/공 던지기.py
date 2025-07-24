# 문제 : 머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120843

# 일단 내 풀이 에서는 아예 아이디어, 수학적 로직이 생각나지 않았다.
def solution(numbers, k):
    answer = 0
    for j in range(k):
        for i in range(0, len(numbers),2):
            if len(numbers) % 2 != 0:

# 단순히 한번 건너뛰고 구하면 될 것 같았다. 그걸 k번 반복 그런데 풀다가 문제를발견한게 k번 하다가 len(numbers)의 값을 넘어가면 어떻게 하지?
# 이런 의문이 들어서 그거 고만하다가 if len(numbers) % 2 홀수 일 떄만 그런 경우가 생길 것  같았는데 이것도 아니었다.

# 결국 몰라서

# 다른분들의 풀이를 보니
def solution(numbers, k):
    return numbers[2 * (k-1) % len(numbers)]

# 가장 간결하게 구하면 이거였고.. 아예 내가 생각한게 틀렸다. 조금 더 수학적으로 생각하면 되었다.
# 수학적 머리가 부족해서 생각해내지 못헀다.

def solution(numbers, k):
    idx = 0
    for _ in range(k -1):
        idx = (idx+2) % len(numbers)
    return numbers[idx]

# 조금더 쉽게 풀면 이렇게 되는 거고

# while문으로 나와 비슷하게 생각해서 풀면
def solution(numbers, k):
    idx =0
    count =1
    while count < k:
        idx = (idx + 2) % len(numbers)
        count += 1
    return numbers[idx]

# 이렇게 푸는거고

# 아예 deque 사용해서 회전으로 풀면
from collections import deque

def solution(numbers, k):
    dq = deque(numbers)
    for _ in range(k-1):
        dq.rotate(-2)
    return dq[0]

# 이렇게 풀 수도 있다. 

# 수학적 머리가.. 문제 많이 풀어보면 늘겠지...?????


