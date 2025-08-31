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



# 하지만 원래 정답은 조금 더 쉽게 구할 수 있음(보기좋게)
n=int(input())
a=list(map(int, input().split()))
ave=round(sum(a)/n)
min=123331233131
for idx, x in enumerate(a):
  tmp=abs(x-ave)
  if tmp<min:
    min=tmp
    score=x
    res=idx+1
  elif tmp==min:
    if x>score:
      score=x
      res=idx+1
print(ave, res)

# 조건문을 따지고 들어가면 tmp가 평균과 원소 값 차이의 절댓값을 나타내는 변수이고 이것도 최솟값을 구하는 알고리즘 처럼 가장 작은 수를 구하게 됨
# 그리고 만약 차이가 같아면 점수가 더 큰 수를 출력하고 그마저 같다면 원소의 순서를 출력하는 로직임
