# 해시 연습
import sys
input=sys.stdin.readline
N = int(input())
A=dict()
c1 = map(int,input().split())
for i in c1:
    if i in A:
        A[i] +=1
    else:
        A[i] =1
M = int(input())
c2 = map(int,input().split())
for j in c2:
    if j in A:
        print(A[j])
    else:
        print(0)