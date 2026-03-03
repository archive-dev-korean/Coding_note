# 연습
N=int(input())
l=[]
for _ in range(N):
    i=input()
    l.append(i)
# # pattern=list(l[0])
# pattern=l[0]
# print(pattern)
# for x in range(1,N):
#     for y in range(len(pattern)):
# #         if l[x][y]==l[x+1][y]:
# #             # print(l[x][y])
# #             result+=l[x][y]
# #         else:
# #             result+='?'
# #             # print('?')
# #         # print(y)
#             if pattern[y] != l[x][y]:
#                  pattern[y]='?'
# print(*pattern,sep='')
result=''
for i in range(len(l[0])): #이건 어짜피 다 같은 범위 나오니까 크게 상관 없는 것 같고
    char=l[0][i]     # 이 부분이 핵심이네 첫번쨰 문자열 부터 시작

    for j in range(1,N):
        if l[j][i] != char:
            char='?'
            break
    result+=char
print(result)