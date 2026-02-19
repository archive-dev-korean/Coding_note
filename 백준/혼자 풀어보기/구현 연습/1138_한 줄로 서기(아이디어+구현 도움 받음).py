# 구현 연습
N=int(input())
i=list(map(int,input().split()))
# print(i)
result=[0]* N
for j in range(len(i)):
    cnt=i[j] # 왼쪽에 있어야 할 '더 큰 사람 수' = 왼쪽 빈칸 개수
    h=j+1 #사람 키 
    # k=1
    for pos in range(N): #자리 찾기
        if result[pos] == 0: #빈칸이면
            if cnt==0: # cnt+1 번쨰 빈칸에 도달
                result[pos] =h
                break
            cnt -=1 # 빈칸 하나 지나감

        # if i[j] == len(i)-k:
        #   k+=1
        #  result[len(i)-k]=j
        # elif len(i) -k <0:
        #     break
print(*result)
# 여기까지 그리디로 푼거고
# 최적의 풀이가 있다고 함
# insert메서드 써서 푸는 것 (GPT)
line=[]
for h in range(N,0,-1): #키 큰 사람 부터
    line.insert(i[h-1],h)
print(*line)