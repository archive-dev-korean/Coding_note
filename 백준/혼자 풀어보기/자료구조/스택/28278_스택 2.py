# 자료 구조 연습
import sys
input=sys.stdin.readline
N=int(input())
stk=[]
for _ in range(N):
    i=input().split()
    if i[0]=='1':
        stk.append(i[1])
    elif i[0]=='2':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif i[0]=='3':
        print(len(stk))
    elif i[0]=='4':
        if stk:
            print(0)
        else:
            print(1)
    else:
        if stk:
            print(stk[-1])
        else:
            print(-1)