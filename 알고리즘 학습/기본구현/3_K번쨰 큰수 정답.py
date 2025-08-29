#set 써야함 <-중복제거
#삼중 루프(i가 제일 첫번째, j가 두번째로 큰수, l이 세번째로 큰수)
n, k= map(int, input().split())
num = list(map(int,input().split()))
# a=sorted(num, reverse=True)
res=set()
for i in range(n):
  for j in range(i+1,n):
    for l in range(j+1,n):
      res.add(num[i]+num[j]+num[l])
res=list(res)
res.sort(reverse=True)
print(res[k-1])


#다중 루프 확인 생각은 헀는데.... 정형화 되지 못해 아쉬움
