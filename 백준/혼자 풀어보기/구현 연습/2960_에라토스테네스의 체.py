# 구현 연습
from collections import deque
from math import sqrt
# d=deque()
N,K=map(int,input().split())
# P=
# a=[]
# for i in range(2,N+1):
#     d.append(i)
# # for j in d:
# P.append(d.popleft())
# a.append(P[0])
# # print(P)
# for j in range(1,len(d)):
#     if d[j] % P[0] ==0:
#         a.append(d[j])
#     else:
#         a.append(d.popleft())
# print(a)


# for j in range(N-1):
#     P.append(d.popleft())
#     a[P[0] * (j+1)]
# print(P)

#강의 보고 내가 짜봄

# a=[i for i in range(2,N+1)]
# cnt=0
# # print(a)
# # for i in range(1,len(a)):
# for j in range(2,N+1):
#     for i in range(len(a)-1,-1 ,-1):
#         # print(i,a[i])
#         if a[i] % j==0: # and a[i] > j:
#         #    d.appendleft(a.pop(i))
#             x=a.pop(i)
#             cnt+=1
#             if cnt == K:
#                 print(x)
                # break
# print(P[K-1])
# print(d[K-1])

# 강의 보고 또 해봄
a=[i for i in range(1,N+1)]
# is_true=[True] * len(a)
# is_true[0] = False
# for j in range(3,len(a),2): #2의 배수 지우기
#     is_true[j]=False
# for j in range(5,len(a),3): #3의 배수 지우기
#     is_true[j]=False

    #
    #
    #
    # 이런식으로 들어갈텐데
# 이걸 패턴화 해서
# for i in range(1, int(sqrt(N))): # 제곱근 씌워서 보면 어디까지 봐야 하는지 나옴
#     if is_true[i]: #True 일 때만 돌아라
#         for j in range(is_true[i]*2 -1, len(a),i):
#             is_true[i]=False
# print(a)

# 이게 정석으로 에라토스테네스의 체 구하는 것이고

#문제에서 요구하는 조건을 구하려면
is_true=[False] * (N+1)
cnt=0
for p in range(2,N+1):
    if is_true[p]:
        continue
    for x in range(p, N+1, p):
        if not is_true[x]:
            is_true[x] = True
            cnt+=1
            if cnt==K:
                print(x)
                break
    if cnt==K:
        break