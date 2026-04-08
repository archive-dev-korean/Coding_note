# 그래프 연습
from collections import deque
N,M=map(int,input().split())
adj=[[0] * (N+1) for _ in range(N+1)] 
for _ in range(M):
    A,B=map(int,input().split())
    adj[A][B]=adj[B][A]=1
# print(*adj)
def bfs(start):
    # visited=[0] * (N+1) # 함수 안으로 선언 해야함
    visited=[-1] * (N+1) # -1 로 초기화 하는게 나중에 계산할 때 편함
    d=deque()
    d.append(start)
    # visited[start]=1
    visited[start]=0
    while d:
        now=d.popleft()
        for nxt in range(1,N+1):
            # if adj[now][nxt]==1 and visited[nxt]==0:
            if adj[now][nxt]==1 and visited[nxt]==-1: #그럼 여기도 visited -1로 조건 바꿔줘야 함
                visited[nxt]=visited[now]+1
                d.append(nxt)
    # return sum(visited[1:]) - N #거리의 합
    return sum(visited[1:])  #거리의 합 -1로 초기화 되어 있을 때
# for i in range(1,N+1):
    # print(bfs(i))
    # 이렇게 적으면 각 노드 마다 거리가 나오게 되고

min_value=999999  # 최대한 큰수 임의 지정
answer=0
for j in range(1,N+1):
    total = bfs(j)
    if total < min_value:
        min_value = total
        answer=j
print(answer)

# 방문 배열을 함수 안에 정의하는 경우 -> BFS/DFS를 여러 번 돌리면 안
# -> 예를 들어 지금은 모든 사람 기준 bfs를 돌아야 되기 때문에 bfs를 여러번 쓰는데 이럴 땐 함수 안에 쓰는 방법 채택
