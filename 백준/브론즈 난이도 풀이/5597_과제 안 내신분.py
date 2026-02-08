# 연습
l=[]
r=[]
for i in range(1,31):
    l.append(i)
# print(l)
for _ in range(28):
    # j=list(map(int,input()))
    j=int(input())
    r.append(j)
for x in l:
    if x not in r:
        print(x)