# 구현 연습
import sys
input=sys.stdin.readline
n=int(input())
l=[]
for _ in range(n):
    i=int(input())
    l.append(i)
# print(sorted(l))
l=sorted(l)
#l.sort() # 이렇게 써도 됨
# 반올림함수 만들어서 round를 그걸로 교체하기
def r(x):
    return int(x+0.5)
# a15=round(len(l) * 0.15) #여기서 에러 나는 것 같은데
a15=r(len(l) * 0.15) #round 대신 r 함수 적용
# print(a15)
avg=0
result=l[a15:n-a15]
# for i in range(a15 -1):
#     if i == 1:
#         result=l[1:]
#     else:
#         result=i[i-1:]
if len(result) ==0:
    avg=0
else:
    avg=r(sum(result)/len(result))
print(avg)
