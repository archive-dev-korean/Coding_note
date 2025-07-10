문제 : 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

def solution(my_string):
    # answer = []
    # s = sort().my_string
    # answer = [filter(lambda x: x==int(), my_string)]
    answer = list(map(int, filter(lambda x: x.isdigit(), my_string)))
    answer.sort()
    return answer

# 사실 isdigit() 함수 써봐서 작성한 것이다. isdigit()는 숫자가 있는지 판별해준다. 람다식이 여기서 거의 처음으로 써서 푼 것 같다.
# 람다식 아직 익숙하지 않지만 많이 써봐야 곘다. 처음 쓸때는 틀렸다.


def solution(my_string):
    answer = [int(x) for x in my_string if x.isdigit()]
    answer.sort()
    return answer

#문론 람다식 쓰지 않고 풀 수도 있다.

def solution(my_string):
    return sorted([int(x) for x in my_string if x.isdigit()])

# sorted() 쓰면 알아서 새로운 리스트로 변환 해준다.
