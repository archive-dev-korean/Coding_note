# 해시 연습
N= int(input())
d=dict()
p= map(int,input().split())
for i in p:
    if i in d:
        d[i]+=1
    else:
        d[i] =1
M=int(input())
r=map(int,input().split())
for i in r:
    if i in d:
        print(d[i])
    else:
        print(0)