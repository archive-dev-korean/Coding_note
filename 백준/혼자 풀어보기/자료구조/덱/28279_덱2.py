# 덱 연습
import sys
input=sys.stdin.readline
from collections import deque
N=int(input())
d=deque()
for _ in range(N):
    # c=list(map(str,input().split()))
    c=input().split() # 이렇게 써도 정답임
    if c[0]=='1':
        d.appendleft(c[1])
    elif c[0]=='2':
        d.append(c[1])
    elif c[0]=='3':
        if len(d)>0:
            print(d.popleft())
        else:
            print(-1)
    elif c[0]=='4':
        if len(d)>0: #if d: 이렇게 써도 됨
            print(d.pop())
        else:
            print(-1)
    elif c[0]=='5':
        print(len(d))
    elif c[0]=='6':
        if len(d)>0:
            print(0)
        else:
            print(1)
    elif c[0]=='7':
        if len(d)>0:
            print(d[0])
        else:
            print(-1)
    else:
        if len(d)>0:
            print(d[-1])
        else:
            print(-1)