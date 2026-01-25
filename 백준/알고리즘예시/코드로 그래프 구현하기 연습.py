# 1. 인접행렬로 DFS 구현 예시 (노드가 13개 있다고 가정)
# adj = [13*13] 으로 가정함

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1 
# for row in adj:
#     print(row)

#dfs 구현(재귀)
def dfs(now): # 현재 방문하는 노드를 인자로 받음
    for nxt in range(13):
        if adj[now][nxt]: # 간선이 있을 때만
            dfs(nxt)

# dfs(0) #을 했을 때 1이,7 이 호출되고 
# 1 이 호출 되었으니 2,5 가 호출 될 것

#BFS 구현(큐)
from collections import deque
adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1 

def bfs():
    dq = deque()
    dq.append(0)
    while dq: #비어 있을 때 까지 반복(비어 있지 않다면)
        now=dq.popleft() #현재 살표보는 노드
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)

bfs()