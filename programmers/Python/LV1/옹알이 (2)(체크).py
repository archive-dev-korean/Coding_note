# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/133499

# 내 풀이
def solution(babbling):
    answer = 0
    dic={'aya':0, "ye":1, "woo":2, "ma":3}
    for i in babbling:
        for j in dic:
            if i == j:
                answer+=1
            # elif j
        
    return answer
# 딕셔너리 만들어서 풀기 근데 테스트 케이스도 하나 맞춤

# 정답: 
def solution(babbling):
    answer = 0
    dic = {'aya':0, 'ye':1, 'woo':2, 'ma':3}
    keys = list(dic.keys())

    for w in babbling:
        i = 0
        ok = True
        last = ""  # 직전에 쓴 키
        while i < len(w):
            matched = False
            for key in keys:
                if key == last:
                    continue  # 같은 음절 연속 금지
                if w.startswith(key, i):
                    i += len(key)
                    last = key
                    matched = True
                    break
            if not matched:
                ok = False
                break
        if ok:
            answer += 1
    return answer

# 어려운데 다른 사람 코드 보면서 공부 해야 할 듯
