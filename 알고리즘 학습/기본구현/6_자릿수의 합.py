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
