# 백준으로 연습 이후 풀이 해시
def solution(clothes):
    # print(clothes)
    answer = 1
    result=dict()
    # dict저장하는 법도 오랜만에 하니까 까먹었고... 샤갈
    for i,j in clothes: #언패킹도 하 ㅅㅂ.. 
        if j in result:
            result[j] +=1
        else:
            result[j] =1
    # print(result)
    
    # 이 부분이 헷갈리네 샤갈 난 물골드 인가...
    for x in result.values():
        # print(x)
        answer *= (x+1)
    return answer -1

        
# 진심으로 이정돈 풀어야 돼....
# 마지막 부분 제외하더라도..