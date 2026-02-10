# 구현 연습
import sys
input=sys.stdin.readline
N,S,P=map(int,input().split())
l=list(map(int,input().split()))
print(l)
for i,j in enumerate(l):
    if S == j:
        print(i+1)