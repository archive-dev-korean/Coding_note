# 구현 연습
import sys
input=sys.stdin.readline
N,S,P=map(int,input().split())
l=[]
if N>0: # 이거 해줘야 안틀림
    l=list(map(int,input().split()))
# print(l)
# for i,j in enumerate(l):

if len(l)==P and S <= min(l):
    print(-1)
else:
    l.append(S)
    l.sort(reverse=True)
    rank = l.index(S)+1 # 가장 앞에 있는 S의 위치를 반환 -> 즉 동점도 가장 앞에 수 나타냄
    print(rank)
    # if len(l)==N and S == l[N-1]:
    #     print(i+1)
        # print(-1)