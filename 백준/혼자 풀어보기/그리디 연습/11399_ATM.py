# 그리디 연습
N=int(input())
# P=list(map(int(input().split())))
P=list(map(int,input().split()))
# print(P)
P.sort()
# print(P)
answer=0
result=0
for i in P:
    answer+=i
    result+=answer
print(result)