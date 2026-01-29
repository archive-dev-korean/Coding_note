# 구현 연습
import sys
input=sys.stdin.readline
K = int(input())
lst=[]
for _ in range(K):
    n=int(input())
    if n == 0:
        lst.pop(-1)
    else:
        lst.append(n)
print(sum(lst))
