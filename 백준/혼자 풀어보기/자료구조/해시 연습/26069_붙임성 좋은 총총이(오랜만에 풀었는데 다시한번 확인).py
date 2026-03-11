# 해시 연습
N=int(input())
# d=dict()
# result=[]
# dance={'ChongChong'} # set일 때 활용
dance={'ChongChong':True}
for _ in range(N):
    i,j=map(str,input().split())
    # print(i,j)
# dict() 으로 풀리나 시도 -> 안풀림
#     if i in d:
#         result.append(i)
#     else:
#         d[i]=j
# print(result)
# print(d)

# 다른 방식은(set)
#     if i in dance or j in dance:
#         dance.add(i)
#         dance.add(j)
# print(len(dance))

#dict로 재시도
    if i not in dance:
        dance[i]=False
    if j not in dance:
        dance[j] =False
    if dance[i] or dance[j]:
        dance[i] = True
        dance[j] = True
print(sum(dance.values())) #이렇게 적으면 True 값만 계산함