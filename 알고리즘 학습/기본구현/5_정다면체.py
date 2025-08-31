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
