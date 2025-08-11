# 문제 : 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    # 1. 평균 점수 리스트 만들기
    avg_list = [sum(row) / len(row) for row in score]
    
    # 2. 평균 점수 내림차순 정렬
    sorted_avg = sorted(avg_list, reverse=True)
    
    # 3. 순위 계산
    answer = [sorted_avg.index(a) + 1 for a in avg_list]
    
    return answer

# 이렇게 풀면 쉽게 풀 수 있다. 순위 구하는 방식이 익숙하지 않을 수 있다. 

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

# 이렇게도 구할 수 있는데 이게 더 여러워 보인다. 하지만 원리는 똑같기 때문에 두 코드는 차이가 유의미하지는 않다.
