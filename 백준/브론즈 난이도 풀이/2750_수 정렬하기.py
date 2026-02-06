# 연습
import sys
input=sys.stdin.readline
N=int(input())
l=[]
# for _ in range(N):
#     i=int(input())
#     l.append(i)
# # l=sorted(l,reverse=False)
# for j in l:
#     print(j)

l=sorted(int(input() for _ in range(N)))
print(*l, sep='\n')

