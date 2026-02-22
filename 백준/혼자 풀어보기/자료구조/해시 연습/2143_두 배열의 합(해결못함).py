# 해시 연습 난이도 : 골드 3
import sys
input=sys.stdin.readline
T=int(input())
m=int(input())
# A=list(map(int,input().split()))
A=[]
line = map(int,input().split())
for x in line:
    A.append(x)

n=int(input())
B= list(map(int,input().split()))
# 완전 탐색?
# A=[]
# B=[]
# for _ in range(m):
#     i=list(map(int,input().split())) # -> m줄로 받을 때, 이렇게 옴
#     A.append(i)
# n=int(input())
# for _ in range(n):
#     j = list(map(int,input().split()))
#     B.append(j)
# print(A)
# print(B)
cnt=0
sum_A=[] # 부분 배열의 합 담길 리스트
sum_B=[] # 부분 배열의 합 담길 리스트

for i in range(n):
    s=0
    for j in range(i,n):
        s+=A[j]
        sum_A.append(s)
        # if i+j ==T:
        #     cnt+=1
for i in range(m):
    s = 0
    for j in range(i,n):
        s += B[j]
        sum_B.append(s)

cnt_B=dict() # B 부분합 카운트 리스트
for x in sum_B:
    if x in cnt_B:
        cnt_B[x] +=1
    else:
        cnt_B[x] = 1

ans = 0
for x in sum_A:
    if T-x in cnt_B:
        ans += cnt_B[T-x]
print(ans)