# 연습
N,M=map(int,input().split())
# l=[[0] * N]
l=[]
for _ in range(N):
    l.append(0)
for _ in range(M):
    i,j,k=map(int,input().split())
    for x in range(i-1,j):
        l[x]=k
# print(l)
# print(l)
print(*l)