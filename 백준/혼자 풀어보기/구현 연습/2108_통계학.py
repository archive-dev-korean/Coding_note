# 구현 연습
import sys
input=sys.stdin.readline
N=int(input())
result=[]
d=dict()
total=0
for _ in range(N):
    i=int(input())
    result.append(i)
    total+=i
    if i in d:
        d[i] +=1
    else:
        d[i] =1
result.sort()

#산술 평균
avg=int(round(total/N))

#중앙값
median = result[N//2]

#최빈값
cnt=max(d.values())
modes=[]
for k,v in d.items():
    if v==cnt:
        modes.append(k)
modes.sort()
mode=0
if len(modes) > 1:
    mode=modes[1]
else:
    mode=modes[0]

# 범위
length=result[-1] - result[0]
print(avg)
print(median)
print(mode)
print(length)
#     average=total//N
#     result.append(average)
#     median=len(d)//len(N)
#     result.append(median)
#     p=0
#     for v in sorted(d.values()):
#         p=d[0]
#         result.append(p)
#     length=max[i] - min[i]
#     result.append(length)

# print(result)