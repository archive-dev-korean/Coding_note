# 해시 연습
N,M = map(int,input().split())
d=dict()
for _ in range(N):
    a,b = map(str,input().split())
    d[a] = b
# print(d.items())
for _ in range(M):
    c = input()
    print(d[c])