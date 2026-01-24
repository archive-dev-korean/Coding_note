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

# combinations 안쓰고 푸는 법 -> 7중 for 문

# 역발상 2개를 뽑으면 7개 뽑는 거랑 같음
h =[int(input()) for _ in range(9)]
h.sort()
tot = sum(h)
for i in range(8):
    for j in range(i+1, 9):
       if tot- h[i] - h[j] == 100:
            for k in range(9):
                if i != k and j != k:
                    print(h[k])
            exit()
            
# 이 것도 중복 일경우 계속 도니까 처리가 필요한데
# 그럴 때, def f(): 정의해서 넣어 버리고 마지막에 return 쓰면 됨
# 다른 방법 -> exit() 쓰면 해결 됨 break 대신