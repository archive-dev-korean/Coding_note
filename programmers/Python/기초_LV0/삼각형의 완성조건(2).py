# 문제 : 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120868

# 일단 경우를 나눠야 하는데 
# 1. 가장 큰 변이 주어졋다고 가정하고 개수 구하기
# 2. 가장 큰 변이 주어지지 않았다고 가정하고 개수 구하기
# 두가지 경우를 합치면 답이 된다.
# 여기까지는 생각함

def solution(sides):
    answer = 0
    n = min(sides) +1
    m = max(sides) +1
    while 1:
        if max(sides) > n + min(sides):
            n += 1
            answer +=1
        elif m <min(sides) + max(sides) and m > max(sides):
            answer +=1
          
    # max(sides)
    return answer
# 그래서 관련 코드를 짰는데 시간이 너무 길어져서 결과가 안나옴 그리고 조건도 조금 이상함
# 올바르게 고치면

def solution(sides):
    answer = 0
    a, b = sides
    a, b = min(a, b), max(a, b)

    x = b - a + 1  # 가능한 시작
    while x < a + b:
        answer += 1
        x += 1
    return answer

# 이건데 이것도 어떻게 생각함? 난 솔직히 모르겠음

# 그래서 다른 사람풀이를 봤는데
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1


def solution(sides):
    return 2 * min(sides) - 1

# 이렇게 풀었던데 이건 어떻게 해야 생각 하는 거지? 수학과인가? 암튼 이것도 정석대로 풀기 어려운 것 같다. 
# 아이디어는 생각했지만 구현이 조금 어려웠다 이번 경우

