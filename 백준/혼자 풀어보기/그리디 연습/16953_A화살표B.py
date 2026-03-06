#그리디 연습
A,B=map(int,input().split())
# 거꾸로 연산하는 것
cnt=0
while B>A:
    if B%10==1:
        B//=10
        cnt+=1
    elif B%2==0:
        B//=2
        cnt+=1
    else:
        break
if B==A:
    print(cnt+1)
else:
    print(-1)
#생각 해내는게 어려움