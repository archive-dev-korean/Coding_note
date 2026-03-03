# 그리디 연습
import sys
input=sys.stdin.readline
# L,R=map(int,input().split())
L,R=input().split()
cnt=0
if len(L)!=len(R):
    print(0)
else:
    for i in range(len(L)):
        if L[i] ==R[i]:
            if L[i]=='8':
                cnt+=1
        else:
            break
    print(cnt)

# if 8 in L or R:

  # for i in range(8,L,10):
#     if L>=8:
#         cnt+=1
#     elif R>=18:
#         cnt+=1
