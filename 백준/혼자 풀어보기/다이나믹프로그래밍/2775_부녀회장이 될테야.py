# DP연습
# 브론즈1 난이도
#시도1 Top - Down 방식
# cache=[-1]
# cache[0]=0
# cache[1]=1
# def f(n):
#     # s=0
#     if n>=0:
#         cache[n+1]=cache[n-1]+cache[n-2]
#     return cache
# print(f(3))
# T=int(input())
# for _ in range(T):
#     k=int(input())
#     n=int(input())
#     for _ in range(k):
#         print(f(n)*k)
#         continue
        
# print(f(7))
# for _ in range(T):
#     f(k)

#시도2 Bottom-UP 방식
T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())

    dp=[i for i in range(1,n+1)] #0층 초기화

    for _ in range(k):
        for i in range(1,n):
            dp[i] +=dp[i-1]
    print(dp[n-1])