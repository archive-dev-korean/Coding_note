# 투 포인터 연습
import sys
input=sys.stdin.readline
N=int(input())
a=[]
s=0
cnt=0
end=0
# for i in range(1,N+1):
#     a.append(i)
# # print(a)
# for j in range(N):
#     # seen=[]
#     while s < N:
#         s+=a[end]
#         end+=1
#     if s ==N:
#         cnt+=1
#     s-=a[j]
# print(cnt)

# 여기까지 투포인터 나름대로 작성 한거고 위에 돌리면 메모리 초과 뜸
# 누적합 이용해서 구하면
prefix=0
seen={0:1}
for x in range(1,N+1):
    prefix +=x
    if prefix - N in seen:
        cnt += seen[prefix - N]
    
    #현재 prefix를 기록
    if prefix in seen:
        seen[prefix] +=1
    else:
        seen[prefix] =1
print(cnt)

# 이 방법도 메모리 초과 뜸 결국 *해결못합*