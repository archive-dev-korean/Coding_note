# 구현 연습
import sys
input=sys.stdin.readline
N=input().strip() # \n 제거
d=dict()
cnt=1 #세트는 최소 1개 필요 하기 떄문
for i in range(9):
    d[i] =1
    if i == 6:
        d[i] +=1
for j in N:
    x=int(j)
    if x==9:
        x =6
    # 아래 부분 완전 엉망
    # for y in j:
    # if x in d:
    #     d[x] -=1
    # elif x==9:
    #     d[6] -=1
    # elif d[x] == 0:
    #     cnt+=1
    #     # 새로운 세트를 추가 해줘야함
    #     d={i for i in range(9)}
    #     d[6] +=1 
    #     continue
    # 새로 작성
    if d[x] >0: # value 값이 0보다 커야 돌기 때문에
        d[x] -=1
    else: # 0 보다 크지 않으면 즉, 0 이면
        cnt += 1
        for k in range(9):
            d[k] +=1
        d[6] +=1
        # 마지막에 이거 추가해 주는 이유가 세트 한번 돌고 말게 아니라 세트 몇번 도는지 확인하기 위해 세트를 다시 초기화 해줘야 함.
        d[x] -= 1

print(cnt)