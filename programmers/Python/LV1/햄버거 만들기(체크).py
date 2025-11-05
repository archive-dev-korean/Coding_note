# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/133502

# 내 풀이 방식은 리스트를 순환 하면서 되는 경우의 수를 판단하여 되면 +1 없으면 그대로 이렇게 생각했었다
# 그래서
def solution(ingredient):
    answer = 0
    lst = []
    for i in range(len(ingredient)):
        lst.append(ingredient[i:i+4])
    for j in lst:
        if j == [1,2,3,1]:
            answer+=1
    return answer

# 이렇게 적었는데 테스트 케이스는 당연히 통과했지만, 채점했을 땐 많이 틀렸다
# 그러다 stack방식으로 되는 수를 빼면 된다는 것도 다른 사람의 코드를 보고 이해했다

def solution(ingredient):
    answer = 0
    stack = []
    
    for x in ingredient:
        stack.append(x)
        # 마지막 4개가 [1,2,3,1]인지 확인
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            del stack[-4:]
    
    return answer

# 처음엔 왜 그러지 했는데 실제로 경우의 수에 대입해보니까 알겠다...
