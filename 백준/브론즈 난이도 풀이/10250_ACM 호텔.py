# 연습
T=int(input())
arr=[]
for _ in range(T):
    a,b,c=map(int,input().split())
for i in range(1,a+1):
    for j in range(1,b+1):
        m=j//10
        n=j%10
        if i==1:
            arr.append(1,m,n)
        print(arr)