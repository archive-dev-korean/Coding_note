# 완전 탐색으로 푸는 문제
from itertools import combinations
# v=[int(input()) for _ in range(9)]
v=[]
for i in range(9):
    n= int(input())
    v.append(n)
    # print(v)
for j in combinations(v,7):
    # print(j)
    if sum(j) ==100:
        # print(j)
        for k in sorted(j):
            print(k)

# 근데 이 위에 코드는 틀렸음 왜냐면 합해서 100이 되는 경우가 여러개 인경우 답이 여러개가 나옴
# 하지만 문제에서 요구하는 조건은 경우가 여러개일 때, 아무 경우의 수만 출력하는 것이기 떄문에 
# 마지막에 break 적어야 됨
        break