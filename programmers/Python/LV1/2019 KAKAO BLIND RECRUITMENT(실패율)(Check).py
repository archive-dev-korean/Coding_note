# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 음 일단 내 풀이는 스테이지 수 만큼 루프 돌아서 stages에서 N보다 작은 수 구해서 실패율 구하고 answer에 저장 한다음, 내림차순 정렬해서 스테이지 값을 구하면 된다고 생각함

# def solution(N, stages):
#     answer = []
#     for i in range(1,N+1):
#         cnt=0
#         ratio=0
#         for j in stages:
#             if j >=i:
#                 cnt+=1
#                     if j<=i:
#                         ratio = j/cnt
#                         answer.append(ratio)
#     return answer
# 뭐 대충 이런식으로 했던 것 같은데 완전히 틀렸고
def solution(N, stages):
    answer = []
    for i in range(1, N + 1):
        reached = 0  # i 이상
        stuck = 0    # i 에서 멈춤

        for s in stages:
            if s >= i:
                reached += 1
            if s == i:
                stuck += 1

        if reached == 0:
            fail = 0
        else:
            fail = stuck / reached

        answer.append((i, fail))
        
    answer.sort(key=lambda x: (-x[1], x[0]))  # 실패율 내림차순 + 스테이지 번호 오름차순 정렬
    return [stage for stage, _ in answer]

# 이렇게 하면 맞는다 
