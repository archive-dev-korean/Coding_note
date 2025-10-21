# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    match_dic = {name[i] : yearning[i] for i in range(len(name))}
    for j in photo:
        s =0
        for k in j:
            if k in match_dic:
                s += match_dic[k]
            else:
                s += 0
        answer.append(s)
    return answer

# 딕셔너리 사용
