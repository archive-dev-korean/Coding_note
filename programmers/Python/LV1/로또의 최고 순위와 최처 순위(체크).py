# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/77484

# 내 방식 풀이 :
# 내부에 등수 구하는 함수 안쓰고 if문으로만 풀었다
def solution(lottos, win_nums):
    answer=0
    match=0
    cnt=0
    for i in lottos:
        if i ==0:
            cnt+=1
        elif i in win_nums:
            match += 1
            
    if match+cnt >1:
        best = 7- (match+cnt)
    else:
        best=6
    
    if match >1:
        worst = 7 - match
    else:
        worst = 6
    return [best,worst]

# 그러나 첫번째 접근할 때는 생각은 맞았으나 구현 하는 데에서 애를 좀 먹음
def solution(lottos, win_nums):
    answer = []
    for i in lottos:
        if i not in win_nums:
            answer.append(len(lottos) - len(i))
            if len(lottos) - len(i) ==0:
                answer.append(1)
            elif len(lottos) - len(i) ==1:
                answer.append(2)
            elif len(lottos) - len(i) ==2:
                answer.append(3)
            elif len(lottos) - len(i) ==3:
                answer.append(4)
            elif len(lottos) -len(i) ==4:
                answer.append(5)
            else:
                answer.append(6)

        
            if i ==0:
                answer.append(len(lottos) - len(i) + i):       
    return answer
  
# 틀린 답이다 애초에 엉망이다

# 그러다 다른 사람의 풀이를 보니
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
# 이렇게 생각할 수도 있구나 했다..

