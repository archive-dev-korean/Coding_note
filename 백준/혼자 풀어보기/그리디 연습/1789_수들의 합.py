# 그리디 연습
import sys
input=sys.stdin.readline
S=int(input())
n=0
s=0
# while True:
#     n+=1
#     s+=n
#     if s>S:
#         break
# print(n-1)

# 작은수(1)부터 높여나가 최대값을 찾는다 -> greedy
# 합 구하는 공식 써볼까?
# K(K+1)/2
while True:
    n+=1
    if n*(n+1)//2 > S:
        break # break 시점에서 n이 나옴 즉 커질 때 n으로 멈춤 
print(n-1) # 그래서 커지기 직전 값 까지만 출력
# 이렇게 풀어도 맞긴함