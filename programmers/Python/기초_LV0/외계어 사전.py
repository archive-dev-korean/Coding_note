# 문제 : PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120869

# set()을 써서 비교해서 풀면 쉽게 풀 수 있다.
def solution(spell, dic):
    spell_set = set(spell)
    
    for word in dic:
        if set(word) == spell_set and len(word) == len(spell):
            return 1
    return 2

# 이렇게 어짜피 문자열과 문자열을 가진 리스트 값을 set()하면 똑같이 출력되기 때문에 비교 연산자 써도 된다.

# 다른 방법도 있는데

def solution(spell,dic):
    spell_sorted = sorted(spell)
    for i in dic:
        if sorted(i) == spell_sorted:
            return 1
    return 2

# 정렬을 사용하는 것이다. 임의로 문자를 섞어서 단어를 표현한다면 섞은 단어를 정렬해서 비교해도 문제없기 때문이다
