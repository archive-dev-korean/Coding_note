# # 구현 연습
# N=int(input())
# l=[]
# cnt=0
# for _ in range(N):
#     i=int(input())
#     l.append(i)
# print(l)
# for j in range(1,N):
#     if l[0] == l[j]:
#         cnt=1
#     elif l[0] > l[j]:
#         cnt=0
#     else:
#         l[j] -=1 
#         cnt+=1
#         l[0] +=1

N=int(input())
l=[int(input()) for _ in range(N)]
cnt=0
if N == 1:
    print(0)
else:
    # while True:
    #     mx=max(l[1:])
    #     if l[0] > mx:
    #         break
    #     idx = l[1:].index(mx) + 1 # 최댓값의 위치값
    #     l[idx] -=1
    #     l[0] +=1
    #     cnt+=1
    while True:
        max_idx =1
        for i in range(2,N):
            if l[i] > l[max_idx]:
                max_idx=i
        if l[0] > l[max_idx]:
            break
        l[max_idx] -=1
        l[0] +=1
        cnt+=1
    print(cnt)