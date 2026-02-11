# 구현 연습
N=int(input())
l=list(map(int,(input().split())))
# print(l)
# cnt=2
# for i in range(2,N):
#     # if i>1:
#         # if l[i] == l[i-1] or l[i] - l[i-1] == l[i-1] - l[i-2]:
#         #     print(l.index(i))
#         # else:
#             # print(2)
#     if l[i] - l[i-1] == l[i-1] - l[i-2]:
#         cnt+=1
#     else:
#         cnt=2
#     max_len=max(2,cnt)
# print(max_len)

# 이거 등차 수열처럼 구했는데 그러면 문제 조건이랑 안맞아서
# 단조수열? 이용해야 함 -> 이거 개념 몰랐음
inc = dec =1 #비내림, 비오름 길이
ans=1 #N이 항상 1이상 이라는 조건이 있어서 1로 줌
for i in range(1,N):
    # 비내림(같아도 이어짐)
    if l[i] >= l[i-1]:
        inc+=1
    else:
        inc=1
    #비오름
    if l[i] <= l[i-1]:
        dec+=1
    else:
        dec=1
    ans = max(ans,inc,dec)
print(ans)
