N=int(input().strip())
student=list(map(int,input().split()))
avg= round(sum(student)/N)

best_idx =0
best_diff=abs(student[0]- avg)
best_score=student[0]
for i in range(N):
  diff = abs(student[i] - avg)
  if (diff < best_diff or
          (diff == best_diff and student[i] > best_score) or
          (diff == best_diff and student[i] == best_score and i < best_idx)):
          best_diff = diff
          best_score = student[i]
          best_idx = i

    # student[i]=student[i]
print(avg, best_idx + 1)
