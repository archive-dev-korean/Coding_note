# 그래프 연습
from collections import deque
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
N,M=map(int,input().split())
# adj=[[0] * (N+1) for _ in range(N+1)] #메모리 초과 날 것 같아서
adj=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,input().split())
    adj[B].append(A)
    # print(bfs(B))
# print(adj)

# 여기서 bfs 호출
# result = [0] * (N+1)

# for i in range(1,N+1):
#     result[i]=bfs(i)
# max_cnt=max(result)
# for i in range(1,N+1):
#     if result[i]==max_cnt:
#         print(i,end=' ')
# 이렇게 적어도 되지만 모든 경우에 대해서 bfs를 돌기 때문에 시간 초과

#안 나게 하려면 DFS 써야함
#해보기 아래