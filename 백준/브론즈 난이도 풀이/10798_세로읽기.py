# 연습
l=[]
result=[]
for _ in range(5):
    i=list(input())
    # i=input()
    l.append(i)
    # for j in range(len(i)):
        # print(i[j])
        # print(j)    

# # print(l)
# 아래 항상 헷갈리는 것 같은데 이해해보자
for k in range(15):
    for j in range(5):
        if k<len(l[j]):
            result.append(l[j][k])
print(*result,sep='')