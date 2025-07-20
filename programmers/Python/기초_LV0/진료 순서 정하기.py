# 문제 : 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120835

# 원래
def solution(emergency):
    answer = []
    se=sorted(emergency, reverse=True)
    for i,j in enumerate(se):
        answer.append(i+1)
    return answer
# 여기까지 구하고 각각 대응한 수를 이제 리턴하면 되는데 set()을 써서 대응하는 수를 묶어서 리턴하려고 했었다.
# 하지만 딕셔너리가 조금 더 효율적 인 것 같았다.

def solution(emergency):
    rank = {num: i+1 for i, num in enumerate(sorted(emergency, reverse=True))}
    
    return [rank[num] for num in emergency]
# 이렇게 딕셔너리 쓰면 된다... 아 제발 생각해네
