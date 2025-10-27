# 출처 :https://school.programmers.co.kr/learn/courses/30/lessons/155652
def solution(s, skip, index):
    answer = ''
    dic ={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14, 'p':15, 'q':16,'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
    num = 0
    for i,j in enumerate(s):
        for k in skip:
            if s(i + index) == k:
                (i + index) += 1
            elif (i+index) >= 25:
                (i+index) += 25 - (i+index)
            else:
    return dic[i+index]

# 내맘대로 풀다가 틀림
# 정답
def solution(s, skip, index):
    # 1) skip 제외한 알파벳 목록
    skip_set = set(skip)
    alpha = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in skip_set]

    # 2) 알파벳 -> 인덱스 딕셔너리
    pos = {ch: i for i, ch in enumerate(alpha)}
    L = len(alpha)

    # 3) 변환
    res = []
    for ch in s:
        i = pos[ch]                 # 현재 문자 위치
        ni = (i + index) % L        # index만큼 앞으로 (순환)
        res.append(alpha[ni])
    return ''.join(res)
