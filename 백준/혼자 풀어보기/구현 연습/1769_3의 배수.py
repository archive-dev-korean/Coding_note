# 구현 연습
import sys
input=sys.stdin.readline
X=int(input())
cnt=0
s=0
#이 코드는 내가 하다가 틀린건데
# 좀 찾아보니 해답을 알 것같틈
# 고쳐보겠음
while X >9:
    s=0
    for i in str(X):
        s+=int(i)
        # cnt+=1
    X=s
    cnt+=1
if X%3==0:
    print(cnt)
    print('YES')
else:
    print(cnt)
    print('NO')



# while X>9:
#     #여기서 추가 부분
#     s=0
#     while X>0:
#         #여기에 s랑 X가 들어가야함
#         s+=X%10
#         X//=10
#     X=s # s가 큰 경우 초기화 
#     cnt+=1
#     # if s > 9:
#     #     continue
#     # else:
#     #     break
# if X%3==0:
#     print(cnt)
#     print('YES')
# else:
#     print(cnt)
#     print('NO')
