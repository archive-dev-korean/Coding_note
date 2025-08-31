n,m = map(int,input().split())
n_list=[]
m_list=[]
tmp=[]
# cnt=0
for i in range(n):
  n_list.append(i+1)
for j in range(m):
  m_list.append(j+1)
for k in range(m): # Corrected range
  for l in range(n): # Corrected range
    tmp.append(n_list[l] + m_list[k])
tmp.sort(reverse=False)
freq={}
for x in tmp:
  freq[x] = freq.get(x,0)+1
max_freq=max(freq.values())
modes = [x for x, f in freq.items() if f == max_freq]
modes.sort()
print(*modes)

# 일단 내 방식대로 구했는데 빈도수 세는 거는 gpt도움 받았다.


n,m=map(int, input().split())
cnt=[0]*(n+m+1) # Increased size by 1
max=0
for i in range(1,n+1):
  for j in range(1,m+1):
    cnt[i+j] += 1
for i in range(n+m+1):
  if cnt[i]>max:
    max=cnt[i]
for i in range(n+m+1):
  if cnt[i]==max:
    print(i, end=' ') # Added a space for better output

# 이게 정답 코드임 
# 딕셔너리 안쓰고도 구할 수 있음
