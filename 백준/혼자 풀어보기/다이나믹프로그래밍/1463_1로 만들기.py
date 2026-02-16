# DP연습
# import sys
# input=sys.stdin.readline
# N=int(input())
# cnt=0
# while N>1:
#     if N%3==0:
#         N//=3
#         cnt+=1
#         # break
#     elif N%2==0:
#         N//=2
#         cnt+=1
#         # break
#     else:
#         N-=1
#         cnt+=1
#         # break
# print(cnt)
# 여기까지 그리디로 푼건데 반례로10이 있음 
# 아래에서 DP로 풀어보기
import sys
input=sys.stdin.readline

N=int(input())
dp=[0] * (N+1) 

for i in range(2, N+1):
    # dp[i] = i를 1로 만드는 최소 연산 횟수
    dp[i] = dp[i-1] + 1 # 1일 때1 2일 때 는 if i%2 ==0이라서 아래 돔 이렇게 흘러감
    if i % 2==0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3] +1)
print(dp[N])

#Bottom - Up 방식 
#for 로직 
# 현재 수의 최솟값 =(갈 수 있는 모든 이전 상태 중 최솟값) +1  