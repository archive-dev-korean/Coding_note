# 연습
n=list(map(int,input().split()))
# print(n)
# result=[]
# for i in range(2,len(n)+1):
#     if n[i-1] - n[i-2] == 1:
#         result.append(n[i-1] - n[i-2])
#         # print('ascending')
#     elif n[i-1] -n[i-2] == -1:
#         result.append(n[i-1] - n[i-2])
#         # print('descending')
#     else:
#         result.append(n[i-1] - n[i-2])
#         # print('mixed')
# # print(result)
# for j in result:
#     if j == 1:
#         print('asencding')
#     elif j==-1:
#         print('descending')
#     else:
#         print('mixed')
if n == sorted(n):
    print('ascending')
elif n== sorted(n,reverse=True):
    print('descending')
else:
    print('mixed')