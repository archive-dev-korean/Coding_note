# 그래프 연습
from collections import deque
import sys
input = sys.stdin.readline
N,M,K,X=map(int,input().split())
# adj=[[0] * (N+1) for _ in range(N+1)]  # 인접 행렬로 풀어서 메모리 초과 남
adj=[[] for _ in range(N+1)] #인접 리스트 만들고
for _ in range(M):
    A,B=map(int,input().split())
    # adj[A][B]=1
    adj[A].append(B) # 값 넣어주기
# print(adj)
# visited=[[0] * (N+1) for _ in range(N+1)]# 방문 체크 -> 이거는 모든 시작점 기준 BFS 할 때나 쓰는 구조
visited=[-1] * (N+1)# 거리 배열(visited 역할)
# visited=[]
# adj[X][]=1
# print(adj)
def bfs(start):
    d=deque()
    d.append(start)
    visited[start]=0 #거리 0부터 시작이라
    while d:
        now=d.popleft()
        # 인접 행렬일 때, 아래 
        # for nxt in range(1,N+1):
            # if adj[now][nxt] ==1  and visited[nxt]==-1:
            #     visited[nxt] = visited[now] +1
            #     d.append(nxt)
        # 인접 리스트 일 때, 아래
        for nxt in adj[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                d.append(nxt)

    # return now
bfs(X)
found=False
for i in range(1,N+1):
    if visited[i] == K:
    # bfs(i)
        print(i)
        found = True
    # else:
if not found:
    print(-1)

# 결국 인접 행렬로 풀어서 에러나는 것임(원인) -> 메모리 초과 뜸
# 인접 리스트 활용 해서 다시 풀어볼게
# -> 이번엔 시간 초과... -> import sys로 해결