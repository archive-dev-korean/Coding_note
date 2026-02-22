# 그리디 브론즈 난이도 풀이
N=int(input())
c=[500,100,50,10,5,1]
answer=0
bill=1000-N
for i in c:
    answer+=bill//i
    bill%=i
print(answer)