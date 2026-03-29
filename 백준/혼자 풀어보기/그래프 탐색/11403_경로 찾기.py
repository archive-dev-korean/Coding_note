# 그래프 연습
N=int(input())
adj=[list(map(int,input().split())) for _ in range(N)]
# print(adj)
# dfs로 풀어도 될 것같은데 내생각은
def dfs(now):
    visited[now]=1
    for nxt in range(N):
        if adj[now][nxt]:
            dfs[nxt]
            if visited[nxt] == 1:
                