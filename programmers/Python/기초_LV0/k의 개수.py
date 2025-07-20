# 문제 : 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120887

# 일단 나는 처음에 
def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        if n in k:
            answer +=1
    return answer
# 이렇게 적었는데

# 당연히 자리수 자체를 비교하는게 아니라 올바르게 결과가 나오지 않음
# 자릿수를 분해해야 하나 고민하다가 그건 너무 일이 커질 것 같았다. count()를 쓰면 펺게 구할수 있다는 걸 꺠달음

def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
      answer += str(n).count(str(k))
    return answer

# 하... 제발 익숙해지자 count()사용법
