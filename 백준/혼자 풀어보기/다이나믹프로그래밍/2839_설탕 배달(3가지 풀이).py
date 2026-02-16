# DP연습
N=int(input())
# result=[3,5]
# result.append(N//5)
# result.append(N//3)
# print(result)
# answer=0
# cnt=0
# for i in range(len(result)):
#     answer+=N//result[i]
#     N %= result[i]
#     if N!=0:
#         cnt=answer
#         continue
#     print(answer)
# 이 코드를 조금 처리하면
answer=-1
for i in range(N//5, -1,-1):
    j=N-(i*5)
    if j % 3==0:
        t=j//3
        answer=i+t
        break
print(answer)


# 사실 완전탐색 Greedy로 풀수도 있음
# N=int(input())
# cnt=0
# while N>=0:
#     if N%5 ==0:
#         cnt+=N//5
#         print(cnt)
#         break
#     N-=3
#     cnt+=1
# else:
#     print(-1)

#DP로 푼다면
# N=int(input())
# dp=[-1] * (N+1)
# dp[3] =1
# if N>=5:
#     dp[5] =1
# for i in range(6,N+1):
#     if dp[i-3] != -1:
#         dp[i] = dp[i-3] + 1
#     if dp[i-5] != -1:
#         if dp[i] == -1:
#             dp[i] = dp[i-5] + 1
#         else:
#             dp[i] = min(dp[i], dp[i-5] + 1)
# print(dp[N])

# dp문제로 분류되어 있지만 완전 탐색으로 푸는게 더 직관적인 것 같음
# Greedy