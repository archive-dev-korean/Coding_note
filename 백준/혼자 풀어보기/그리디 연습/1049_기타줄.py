# 그리디 연습
N,M=map(int,input().split())
l=[]
for _ in range(M):
    i=list(map(int,input().split()))
    l.append(i)
# print(l)
# if N//6 < 1:
#     for x in range(M):
#         mini=[]
#         mini.append(N*l[x][1])
#     print(min(mini))

#         # for y in range(len(i)):
#            # M*l[x][1]

# 이런식으로 구하다 보면 결국 완전 탐색으로 풀게 되네...?

# 낱게 최소값 변수, 패키지 최소값 변수 해서 구해야겟다
one_min=min(x[1] for x in l)
pack_min=min(x[0] for x in l)
# print(one_min,pack_min)
if N<6:
    print(min(N*one_min,pack_min))
else:
    print(min((N//6)*pack_min+(N%6)*one_min,((N//6)+1)*pack_min,N*one_min))
    # 마지막으로 낱개 * 최소 값 다 비교 해봐야 안틀림