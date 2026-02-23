# 그리디 연습
N=int(input())
# for _ in range(2):
A=list(map(int,input().split()))
B=list(map(int,input().split()))
# int(input().split())
# print(A)
A.sort()
B.sort(reverse=True)
# print(A)
# print(B)
# print(A*B)
result=0
for i in range(N):
    result+=A[i]*B[i]
print(result)
# print(B.index(max(B)))
# for i,v in enumerate(B):
#     if max(B) == v:
#         # print(i)
#         A[i]=A[0]
#     elif min(B)==v:
#         A[i]=A[-1]
# print(A)

# 이렇게 풀면 정답은 맞음

#문제 조건에 의하면 B를 완전 탐색해야 하는데 
#그게 오히려 시간 복잡도 늘어남 -> 그리디는 최소가 되는 경우 찾는 건데 그리디 취지에서 벗어남
#그래서 일단 정렬로 푸는게 합리적인 방식임