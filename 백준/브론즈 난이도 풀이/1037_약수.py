# 연습
import sys
input=sys.stdin.readline
N=int(input())
real=list(map(int,input().split()))
A=0 # 이게 result로 나와야 함
# for _ in range(N):
# 아이디어 -> 가장 작은 약수 * 가장 큰 약수 = 원래 수
A=min(real)*max(real)
print(A)

# 문제 이해 능력이 좀 떨어지나?