# 해시 연습
import sys
input=sys.stdin.readline
N=int(input())
d=dict()
for i in range(N):
    p,r=input().split()
    d[p] = r
# for k,v in reversed(list(d.items())):
#     if v == 'enter':
#         print(k)

for k in sorted(d.keys(),reverse=True):
    if d[k] == "enter":
        print(k)