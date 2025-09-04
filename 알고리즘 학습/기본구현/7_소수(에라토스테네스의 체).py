n=int(input())
cnt=set()
for i in range(1,n+1):
  for j in range(2,i+1):
    if i%j==0:
      if j==2:
        cnt.add(j)
        continue
      root = int(j**0.5)
      if root * root == j or j%2 == 0:  
            continue
      cnt.add(j)
print(cnt)  

# 내 방식으로 구한건데 틀림 에라토스테네스의 체 안씀 (로직 오류)

#에라토스테네스의 체 사용
n = int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2,n+1):
  if ch[i]==0:
    cnt +=1
    for j in range(i,n+1,i):
      ch[j]=1
print(cnt)
