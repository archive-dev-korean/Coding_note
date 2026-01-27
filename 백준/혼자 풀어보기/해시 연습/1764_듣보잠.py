#해시 연습
N,M = map(int,input().split())
D= dict()
for i in range(N):
    p=input()
    if p in D:
        D[p] +=1
    else:
        D[p] = 1
for j in range(M):
    r=input()
    if r in D:
        D[r] +=1
    else:
        D[r] =1
result=[]
for k,v in sorted(D.items(),reverse=False):
    if v==2:
        result.append(k)
print(len(result))
for k in result:
    print(k)

#result 부터 끝까지 이렇게 써도 되고,

result=[]
for k,v in D.items():
    if v==2:
        result.append(k)
result.sort()
print(len(result))
for name in result:
    print(name)

#이렇게 써도 됨.