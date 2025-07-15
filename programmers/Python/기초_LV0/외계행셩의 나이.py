# 문제 : 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    mapping = ('a','b','c','d','e','f','g','h','i','j')
    answer = ''.join(mapping[int(digit)] for digit in str(age))
    return answer

# 딕셔너리 사용해서 구하는 방법도 있다.

def solution(age):
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(conv[i] for i in str(age))

# 이런식으로 그런데 digit사용해서 mapping하는게 더 편한 것 같다.
