#해시 연습
N,M = map(int,input().split())
A=dict()
cnt=0
for i in range(N):
    r=input()
    if r in A:
        A[r] +=1
    else:
        A[r] =1
for j in range(M):
    p=input()
    if p in A:
        cnt+=1
print(cnt)
