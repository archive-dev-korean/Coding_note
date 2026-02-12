# DP 알고리즘 예제
# 삼각수 활용한 것임
import sys
sys.setrecursionlimit(10 **8) # Python 기본 재귀 범위 늘려줌
N,K=map(int,input().split())
MOD = 10007 #나머지 
cache=[[0]*1001 for _ in range(1001)] #메모이제이션 적용에 활용
# 시도 1 재귀 방식
# def bino(n,k):
#     if k==0 or k==n:
#         return 1
#     return bino(n-1,k-1) + bino(n-1,k)
# 여기까지 메모이 제이션 안쓴거고

# 여기부터 메모이 제이션 씀
# def bino(n,k):
#     if cache[n][k]: #0이 아닌수(양수 라면)
#         return cache[n][k]
#     if k==0 or k==n:
#         cache[n][k] =1
#         # return 1
#     else:
#         cache[n][k]=bino(n-1,k-1) + bino(n-1,k)
#         cache[n][k] %= MOD #나머지 
#     return cache[n][k]

# print(bino(N,K))


#시도 2 반복문
for i in range(1001):
    cache[i][0] = cache[i][i] =1 
    for j in range(1,i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD
# for i in range(7):
    # print(cache[i])
# print()
print(cache[N][K])