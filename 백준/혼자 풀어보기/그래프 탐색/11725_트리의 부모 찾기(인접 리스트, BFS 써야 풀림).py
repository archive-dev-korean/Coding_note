# 그래프 연습
N=int(input())
adj=[[0]*(N+1) for _ in range(N+1)]
# print(*adj)
for _ in range(N-1):
    v1,v2=map(int,input().split())
    adj[v1][v2]=adj[v2][v1]=1 #무방향 그래프로 돌거고
#DFS
def dfs(now):
    visited[now]=1 # 방문한 노드 기록
    # print(visited)
    for nxt in range(1,N+1):
        if adj[now][nxt] and not visited[nxt]:
            parent[nxt]=now #이게 들어가야함
            dfs(nxt)
#여기서 부모를 체크 해줘야 하니까
parent=[0] * (N+1) # 이게 들어가고(부모 노드 체크)
visited=[0] * (N+1) # 방문노드
dfs(1)
for i in range(2,N+1):
    print(parent[i])

# 인점 행렬을 쓰면 메모리 초과 나고 인접 리스트 써야함
# 그리고 BFS로만 풀어야 에러 안남
import sys
from collections import deque
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
visited = [0] * (N+1)

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

#dfs로 풀면 런타임 에러남
# def dfs(now):
#     visited[now] = 1
#     for nxt in graph[now]:
#         if not visited[nxt]:
#             parent[nxt] = now
#             dfs(nxt)

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                parent[nxt] = now
                q.append(nxt)

bfs(1)

for i in range(2, N+1):
    print(parent[i])