# 연습
N,M=map(str,input().split())
answer=[]
result=[]
# for i in range(int(N),0,-1):
#     print(i)
    # answer.append(i)
answer.append(N)
answer.append(M)
# print(answer)
for i in answer:
    # for j in i:
    reverse=i[::-1]
    result.append(reverse)
# print(result)
if  result[0] > result[1]:
    print(result[0])
else:
    print(result[1])
# for j in range(M,0,-1):
#     answer.append(j)
# print(answer)

a,b = input().split()
print(max(int(a[::-1]), int(b[::-1])))

