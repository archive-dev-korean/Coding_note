# 문제 : 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요

def solution(sides):
    answer = 0
    max(sides)
    for i in sides:
        if i < max(sides):
            sum(i - max(sides))
            if  sum(i - max(sides)) > max(sides): 
                 return 1
            else:
                return 2
        else:
            pass

# 풀다 보니 내가 다 헷갈려서 다른 방법을 찾았다.

def solution(sides):
    answer=0
    max_side = max(sides)
    total = sum(sides) - max(sides)
    if max_side < total:
        return 1
    else:
        return 2

  # 이 방법을 썻다 max는 내장함수라 import없이 써도 된다.

# 위에 코드도 괜찮지만 진짜 python 스럽게 풀려면
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

# 이렇게 쓰면 된다.
