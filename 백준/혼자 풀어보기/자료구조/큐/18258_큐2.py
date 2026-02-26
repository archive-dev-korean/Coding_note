# 구현 연습
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
q=deque()
for _ in range(N):
    x=input().split()
    if x[0] == 'push':
        q.append(x[1])
    elif x[0] =='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif x[0] =='size':
        print(len(q))
    elif x[0] =='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif x[0]=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])