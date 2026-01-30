# 구현 연습
import sys
input=sys.stdin.readline
N,M = map(int,input().split())
arr=[]
for _ in range(N):
    i=list(map(int,input().split()))
    arr.append(i)
# print(arr)
K=int(input())
# for _ in range(K):
#     i,j,x,y = map(int,input().split())
#     total =0
#     for r in range(i-1,x):
#         for c in range(j-1,y):
#             total +=arr[r][c]
#     print(total)

# 이거 시간 초과 발생 함..




# 누적합 구해서 풀기 GPT

# 2차원 누적합 (N+1) x (M+1)
dp =[[0] * (M+1) for _ in range(N+1)]
# print(dp)
for r in range(1,N+1):
    row_sum=0
    for c in range(1,M+1):
        row_sum += arr[r-1][c-1]
        dp[r][c] = dp[r-1][c] + row_sum
for _ in range(K):
    i,j,x,y=map(int,input().split())
    total = dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]
    print(total)
