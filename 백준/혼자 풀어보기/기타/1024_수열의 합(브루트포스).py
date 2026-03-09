# 부르트포스 알고리즘 연습
import sys
input=sys.stdin.readline
N,L=map(int,input().split())
found=False # flag-> 상태 저장 변수 값
# result=[]
# i=1
s=0
# while True:
#     i+=1
#     s+=i
#     if s==N:
#         for _ in range(L):
#             result.append(i)
#             i-=1
#     elif s>N:
#         break
# print(result)
# 이렇게 풀면 100% 시간 초과
# # x=(2*N-L-1)//2*(L+1)
# # print(x)
# for _ in range(L,N):
#     x=0
#     x+=1
#     s+=x
#     if s==N:
#         result.append(x)
# print(result)
# 결국 아까 점화식 으로 푼 것 비슷하게 풀면 돔
# for _ in range(100):
#     x=(N-1)//L #이게 점화식인데 이걸 어떻게 생각하는 거지??
#     if x % L ==0:
for i in range(L,101):
    temp=N-i*(i-1)//2 # len*x=N-len(len-1)//2 이 부분
    if temp < 0:
        break
    if temp % i ==0: # x가 정수 일 경우 (len으로 나누어 떨어지면 정수임)
        result=temp//i # x를 구하는 것 x=(N-len(len-1)//2) // len 이부분
        if result>=0:
            for j in range(i):
                print(result+j,end=' ')
            found=True
            break
if found==False:
    print(-1)

#점화식 생각해내기 개빡세네 -> 점화식으로 풀어야 한다는 것은 떠올림
# 연속된 수열 x, x+1, x+2, ... , x+len-1
# 길이가 4 이면
# x, x+1, x+2, x+3
# 합= x+(x+1)+(X+2)..(x+len-1)
# x는 len 개
# 그래서 len*x 
# 나머지 부분
# 0+1+2...+(len-1) -> len(len-1)//2
# 그래서
# N=len*x+len(len-1)//2
# x를 구하는 식
# len*x=N-len(len-1)//2
# x=(N-len(len-1)//2) // len