def solution(order):
    answer = 0
    for i in str(order):
        if int(i) in [3,6,9]:
            answer+=1
    return answer

# 가장 정석 풀이

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

# 이렇게도 풀 수 있음
