# 그래프 연습
from collections import deque
import sys
sys.setrecursionlimit(10 **6)
input=sys.stdin.readline
def bfs(now):
    visited=[0] * (N+1)
    d=deque()
    d.append(now)
    visited[now]=1
    cnt=1 # 세줘야 함 이거 생각 못함
    while d:
       cur=d.popleft()
       for nxt in adj[cur]:
           if not visited[nxt]:
               visited[nxt]=1
               d.append(nxt)
               cnt+=1
    return cnt
#안 나게 하려면 DFS 써야함
#해보기 아래
def dfs(now):
    cnt=1
    visited[now]=1
    for nxt in adj[now]:
        if visited[nxt]==0:
            visited[nxt]=1
            cnt+=dfs(nxt)
            # dfs(nxt)
    return cnt
N,M=map(int,input().split())
# adj=[[0] * (N+1) for _ in range(N+1)] #메모리 초과 날 것 같아서
adj=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,input().split())
    adj[B].append(A)
    # print(bfs(B))
    # print(dfs(B))
# print(adj)

# 여기서 bfs 호출
# result = [0] * (N+1)

# for i in range(1,N+1):
#     visited=[0] * (N+1)
#     visited[i]=1 #시작점 방문 처리
#     # result[i]=bfs(i)
#     result[i]=dfs(i)

result = [0] * (N + 1)
visited = [0] * (N + 1)

for start in range(1, N + 1):
    stack = [start]
    visited[start] = start
    cnt = 1

    while stack:
        cur = stack.pop()
        for nxt in adj[cur]:
            if visited[nxt] != start:
                visited[nxt] = start
                cnt += 1
                stack.append(nxt)

    result[start] = cnt
max_cnt=max(result)
for i in range(1,N+1):
    if result[i]==max_cnt:
        print(i,end=' ')
# 이렇게 적어도 되지만 모든 경우에 대해서 bfs를 돌기 때문에 시간 초과

