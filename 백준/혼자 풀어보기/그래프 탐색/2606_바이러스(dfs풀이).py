# 그래프 탐색 연습
import sys
N=int(input()) #노드
C=int(input()) #간선
adj=[[0]*(N+1) for _ in range(N+1)]
for _ in range(C):
    i,j=map(int,input().split())
    adj[i][j]=adj[j][i]=1
# for x in adj:
#     print(x)
#DFS가 더 편한 것 같은데 
def dfs(now):
    visited[now]=1
    # print(now)
    global cnt
    for nxt in range(N+1):
        if adj[now][nxt] and not visited[nxt]: 
            dfs(nxt)
            cnt+=1
    return cnt
visited=[0] * (N+1)
cnt=0
print(dfs(1))

#BFS로 풀어도 답은 맞을듯