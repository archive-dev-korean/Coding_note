# 그래프 연습
T=int(input())
for _ in range(T):
    N=int(input())
    adj=[[0] * (N+1) for _ in range(N+1)]
    numlist=map(int,input().split())
    adj[b][a]=1