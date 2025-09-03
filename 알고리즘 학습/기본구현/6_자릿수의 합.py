N = int(input().strip())
rows = list(map(int, input().split()))
total_sum = []
for i in rows:
  s = sum(int(d) for d in str(i))
  total_sum.append(s)
max_v=total_sum[0]
result = rows[0]
for j in range(1, len(total_sum)):
  if max_v < total_sum[j]:
    max_v = total_sum[j]
    result = rows[j]
    # print(total_sum[j])
  elif max_v == total_sum[j]:
    if rows[j] > result:
      result = rows[j]
    # max_v=total_sum[j]
print(result)

# 이렇게 썼는데 60점짜리 답이다
#일단 정신없이 구해서 문제에서 요구하는 것을 다 못쓴것도 있다. def사용 같은..

n=int(input())
a=list(map(int,input().split()))

def digit_sum(x):
  sum=0
  while x>0:
    sum+=x%10
    x=x//10
  return sum
max = -13213133
for x in a:
  total=digit_sum(x)
  if total>max:
    max=total
    res=x
print(res)

# 이게 정석적인 풀이이다 x를 10으로 계속 나눠서 하는것 while 써서

def digit_sum(x):
  sum=0
  for i in str(x):
    sum +=int(i)
  return sum
  
for x in a:
  total=digit_sum(x)
  if total>max:
    max=total
    res=x
print(res)

# 이렇게 string처리해서 구해도 똑같음
