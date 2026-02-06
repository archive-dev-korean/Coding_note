# # 연습
N=int(input())
# # while True:
# #     i
# #     total=N*N-1
# # for i in range(1,N+1):
# #     s=i*i+1

# 재귀 함수
# def factorial(n):
#     if n <=1:
#         return 1
#     return n * factorial(n-1) 
# print(factorial(N))

# 안쓰고로직으로만
result=1
for i in range(2,N+1):
    result *=i
print(result)

while N > 1:
    result*=N
    N-=1
print(result)
