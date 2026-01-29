# 구현 연습
from collections import deque
import sys
input=sys.stdin.readline
d=deque()
N=int(input())
for _ in range(N):
    i = input().split()
    if i[0] =='push_front':
        d.appendleft(i[1]) 
    elif i[0] =='push_back':
        d.append(i[1])
    elif i[0] =='pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif i[0] =='pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(d))
    elif i[0] =='empty':
        if d:
            print(0)
        else:
            print(1)
    elif i[0] =='front':
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)


