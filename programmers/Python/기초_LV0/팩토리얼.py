# 문제 : i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

# i! ≤ n

# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120848

# 원래 팩토리얼을 내 방식대로 하려다가
def solution(n):
    answer = 0
    i =1
    while 1:
        i += 1
        answer = i*i
        if max(answer) <= n:
            return i
    # return answer
# 이렇게 적게 되었는데 좀 동작이 이상하게 됨 일단 무한루프 돌아서 구하는 것 까지는 생각했으니까 팩토리얼만 제대로 구하면 되겠다 생각함

def solution(n):
    answer = 1
    i = 1
    while True:
        answer *= i
        if answer > n:
            return i - 1
        i += 1

# 이렇게 구하면 됨. 처음에 i += 1 이게 answer밑 if 위에 있어야 한다고 생각했는데 잘 생각해보니 아니었음 일단 수 비교부터 하고 나서 증가하는게 맞았음


