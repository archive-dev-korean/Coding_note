# 인접 행렬 쓰는게 유리함 -> 간선의 개수가 N^2 급 이라서
# DFS로 일단 풀어보고
# 체크 리스트 만들어서 연결 요소 탐색 해보기
import sys
sys.setrecursionlimit(10 ** 6) #Python은 기본적으로 재귀 함수의 깊이가 10 ** 3으로 제한되어 있는데 이보다 더 깊게 갈 경우 에러 나옴 그래서 늘려주는 방식

input = sys.stdin.readline #input 에서 100만 이상의 수가 문제에서 들어와서 시간 초과 발생 따라서 다른 방식의 인풋 써야함

N,M = map(int, input().split()) 
adj = [[0] * N for _ in range(N)]
for i in range(M):
   a,b = map(int,input().split())
   a -=1
   b -=1
   #or 
#    a,b = map(lambda x:x-1, map(int,input().split())) #왜 이렇게 해주냐면 문제에서 정점의 좌표가 0부터가 아니라 1부터 임
   adj[a][b] = adj[b][a] = 1
# for row in adj:
#    print(row)

#dfs 구현
def dfs(now):
   for nxt in range(N):
      if adj[now][nxt] and not chk[nxt]:
         chk[nxt] = True
         dfs(nxt)

#체크 배열 만들기
chk = [False]  * N
cnt =0
for j in range(N):
   if not chk[j]:
      cnt+=1
      chk[j] = True
      dfs(j)
print(cnt)