# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131128

# 내 풀이 :
def solution(X, Y):
    answer = ''
    Y=list(Y)
    for i in X:
        if i in Y:
            answer += i
            Y.remove(i)
    if not answer:
        return "-1"
    elif set(answer) == {"0"}:
        return '0'
    else:
        
        return ''.join(sorted(answer, reverse=True))

#   이렇게 짜면 시간 초과가 걸림 70점 짜리 답임
# 블로그나 기타 여러 자료를 찾아보니 count방식으로 처리하는 방법을 많이 쓴다

def solution(X,Y):
   x_count = [0] * 10
    y_count = [0] * 10

    # 문자열을 한 번만 순회하면서 개수 계산
    for ch in X:
        x_count[int(ch)] += 1
    for ch in Y:
        y_count[int(ch)] += 1

    result = []

    # 9부터 0까지 내려가며 공통으로 존재하는 개수만큼 추가
    for d in range(9, -1, -1):
        common = min(x_count[d], y_count[d])
        if common > 0:
            result.append(str(d) * common)

    # 공통 숫자가 없는 경우
    if not result:
        return "-1"

    answer = ''.join(result)

    # 결과가 모두 0인 경우
    if answer[0] == "0":
        return "0"

    return answer

# 이렇게 좀 이해 하기 어려울 수 있다

# counter 모듈을 사용하는 방법도 존재한다 하지만 사용법이 익숙하지 않기 때문에
# 해답 코드만 첨부 하겠음
from collections import Counter

def solution(X, Y):
    x_count = Counter(X)
    y_count = Counter(Y)
    
    common = ''
    for num in sorted(x_count.keys(), reverse=True):
        if num in y_count:
            common += num * min(x_count[num], y_count[num])
            
    if not common:
        return "-1"
    if set(common) == {"0"}:
        return "0"
    return common
