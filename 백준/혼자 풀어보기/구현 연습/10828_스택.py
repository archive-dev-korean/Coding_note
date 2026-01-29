# 구현 연습
import sys
input = sys.stdin.readline
N = int(input())
stk =[]
for _ in range(N):
    i=input().split()
    if i[0]=='push':
        stk.append(i[1])
    elif i[0]=='top':
        if stk:
            print(stk[-1])
        else:
            print(-1)
    elif i[0]=='size':
        print(len(stk))
    elif i[0]=='empty':
        print(0 if stk else 1)
    else:
        if stk:
            print(stk.pop())
        else:
            print(-1)