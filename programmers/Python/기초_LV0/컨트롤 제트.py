# 문제 : 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120853

# 그리고 일단 두가지 방법 모두 잘 생각해내지 못한 것이 가장 큰 문제이다

# 일단 간단하게 두가지 풀이로 풀 수 있는데

def solution(s):
    answer = 0
    temp=0
    s = s.split()

    for i in s:
        if i=='Z':
            answer-=temp
            continue
        temp=int(i)
        answer+=int(i)
    return answer

  # 이렇게 푸는것은 더해주는 변수와 뺴는 변수를 각각 지정해서 구하는 방법이고

  
def solution(s):
    stack = []
    for i in s.split():
        if i == 'Z':
            if stack:
                stack.pop()  
        else:
            stack.append(int(i))  
    return sum(stack)

    # 이렇게 푸는건 stack구조를 활용한 pop이용한 것이다.

    # 뭘 쓰든 똑같은 결과와 시간복잡도는 비슷하겠지만 예전부터 pop을 쓰는걸 익숙해지자 라고 했기 때문에 pop쓰는거에 익숙해지지 제발
    
