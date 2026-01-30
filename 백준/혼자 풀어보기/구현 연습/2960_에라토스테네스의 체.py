# 구현 연습
from collections import deque
d=deque()
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
a=[i for i in range(2,N+1)]
cnt=0
# print(a)
# for i in range(1,len(a)):
for j in range(2,N+1):
    for i in range(len(a)-1,-1 ,-1):
        # print(i,a[i])
        if a[i] % j==0: # and a[i] > j:
        #    d.appendleft(a.pop(i))
            x=a.pop(i)
            cnt+=1
            if cnt == K:
                print(x)
                break
# print(P[K-1])
# print(d[K-1])