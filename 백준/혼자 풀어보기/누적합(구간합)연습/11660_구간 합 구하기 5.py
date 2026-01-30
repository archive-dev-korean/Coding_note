# 구간 합 연습 
# 2차원 누적합 임
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
prefix=[[0] * (N+1) for _ in range(N+1)]
# print(prefix)
a=[]
for _ in range(N):
    i = list(map(int,input().split()))
    a.append(i)
# print(a)
# for i in range(len(a)):
#     prefix[i+1] = prefix[i] + a[i-1]
for i in range(1,N+1):
    for j in range(1,N+1):
        prefix[i][j]= prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1] + a[i-1][j-1]
s=0
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    s=prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    # s=prefix[x2-1][y2-1] - prefix[x2-1][y1-1] - prefix[x1-1][y2-1] + prefix[x1][y1]
    print(s)

# 흠 아직은 prefix만드는 거 어려운데 좀 익숙해 져야 할 거 같음