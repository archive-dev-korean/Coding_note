# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    i1 = i2 = 0
    n1, n2 = len(cards1), len(cards2)

    for word in goal:
        if i1 < n1 and cards1[i1] == word:
            i1 += 1
        elif i2 < n2 and cards2[i2] == word:
            i2 += 1
        else:
            return "No"
    return "Yes"


# 또는 deque
from collections import deque

def solution(cards1,cards2,goal):
    c1, c2 = deque(cards1), deque(cards2)
    for i in goal:
        if c1 and c1[0] ==i:
            c1.popleft()
        elif c2 and c2[0] ==i:
            c2.popleft()
        else:
            return "No"
    return 'Yes'

# 또는 
