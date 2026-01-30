# 구현 연습
from collections import deque
d=deque()
N,K=map(int,input().split())
a=[]
P=[]
for i in range(2,N+1):
    d.append(i)
for j in range(N-1):
    P.append(d.popleft())
    a[P[0] * (j+1)]
print(P)