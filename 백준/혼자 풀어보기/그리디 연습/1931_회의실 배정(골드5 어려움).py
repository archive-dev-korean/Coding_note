# 그리디 연습 골드5
import sys
input=sys.stdin.readline
N=int(input())
l=[]
for _ in range(N):
    i=list(map(int,input().split()))
    l.append(i)

# for i in range(1,N):
#    print(l[i]) #입장시간
#    cnt=0
#    if l[0][1] <= l[i][0]:
#        cnt+=1
#        if 
#    print(l[i][1]) #퇴장시간
#    if l[i][1]  
#이런식으로 풀면 완전탐색으로 푸는 거고 이 문제는 그리디 문제임
#내 생각에는 입장시간 기준으로 정하고 풀었는데 그러면 아까 말했듯 완전탐색이 되어 버리고
# 퇴장시간 기준 정렬 후 로직을 짜면 최적해(그리디)가 나옴
# l[-1].sort() #이렇게 하면 안됨
l.sort(key=lambda x:(x[1],x[0])) #이렇게 해도됨
# l.sort(key=lambda x:x[1]) #이렇게 해도됨 아래에서 시작 시간과 끝 시간 조건이 있어서 이렇게 써도 정답은 될거임

# print(l) #lambda 써서 [1] 과 [0]의 위치가 바뀔 줄 알았는데 보니까 안바뀜
cnt=0
end=0
for i,j in l:
    if i>=end:
        cnt+=1
        end=j
    # print(i)
    # print(j)
print(cnt)