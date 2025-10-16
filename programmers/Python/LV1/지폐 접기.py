출처 : https://school.programmers.co.kr/learn/courses/30/lessons/340199

# 90도 접는 로직 
# for문 필요 없음
def solution(wallet, bill):
    answer = 0
    # for i in range(len(bill)):
    #     if bill[i] > wallet[i] or bill[i+1] > wallet[i+1]:
    #         if bill[i] > bill[i+1]:
    #             bill[i]//2
    #         else:
    #             bill[i+1]//2
    #         answer +=1
    # while True:
    #     if (bill[0] > wallet[0] or bill[1] > wallet[1]) or (bill[1] < wallet[0] or bill[1] > wallet[0]):
    #         break
    while (bill[0] > wallet[0] or bill[1] > wallet[1]) and (bill[1] > wallet[0] or bill[0] > wallet[1]):
        if bill[0] > bill[1]:
            bill[0] //=2
            # if bill[1] < wallet[0]:
            #     continue
        else:
            bill[1] //=2
            # if bill[0] < wallet[1]:
            #     continue
        answer +=1
    
    return answer

# 처음에 for문으로 시작했다가 while문으로 바꿈
# 그리고 90도 돌려서 넣는 로직 없이 썼다가 틀려서
# 결국 힌트 받고 문제 풀음
