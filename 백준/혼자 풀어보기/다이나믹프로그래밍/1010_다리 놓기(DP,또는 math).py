# DP연습
from itertools import combinations
import math
T=int(input())
# for _ in range(T):
#     cnt=0
#     N,M=map(int,input().split())
#     for _ in combinations(range(M),N):
#         cnt+=1
#     print(cnt)
# 정답은 맞을 수 있는데 이렇게 풀면 시간 초과
# for _ in range(T):
#     N,M=map(int,input().split())
#     print(math.comb(M,N))
#math 방식으로 풀면 정답이긴 함 근데 정석은 DP 쓰는것

#DP 방식으로 풀어야 함
#Bottom-up 방식으로 풀 수 있고 점화식을 생각해내야 하는데 이게 어려움
# 점화식 C(M,N) = C(M-1,N-1) + C(M-1,N) --> M개중 N개 고르기
dp=[[0] * 31 for _ in range(31)] # 문제에서 입력 범위가 주어져 있음
# print(dp)
for i in range(31):
    dp[i][0] = 1
    dp[i][i]=1
for i in range(1, 31):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        # 여기까지가 파스칼 삼각형 만드는 코드 바로 위에 줄 코드가 왼쪽 위 + 오른쪽 위
for _ in range(T):
    N,M=map(int,input().split())
    print(dp[M][N])
# 파스칼 삼각형 채우는 구조로 dp 리스트 만들고 하나씩 채워가는 구조임