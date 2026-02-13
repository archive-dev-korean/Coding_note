# 연습
n=int(input())
l=[-1] * 21
l[0]=0
l[1]=1
# for i in range(2,n+1):
#     l[i]=l[i-1] + l[i-2]
# print(l[n])

def f(n):
    if l[n]==-1:
        l[n] = f(n-1) + f(n-2)
    return l[n]
print(f(n))