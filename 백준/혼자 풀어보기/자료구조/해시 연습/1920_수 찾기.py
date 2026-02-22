# 해시 연습
import sys
input=sys.stdin.readline
N=int(input())
A=dict()

# for i in range(N):
#     s1 = int(input())
s1 = map(int, input().split())
for i in s1:
    if i in A:
        A[i] +=1
    else:
        A[i] =1
M=int(input())
s2 = map(int,input().split())
# for j in range(M):
#     s2 = int(input())
for j in s2:
    if j in A:
        print(1)
    else:
        print(0)
