# 문제 : 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

def solution(num, k):
    for i,j in enumerate(str(num)):
        if j == str(k):
            return i+1
    return -1

# 리스트 컴프리헨션, 인덱싱 사용하는 방법도 있지만 이렇게 푸는게 가장 간단한 방법 같다.
# 숫자를 문아열로 바꿔서 풀어야 정상 작동함. str(num)이 부분 아니면 타입 에러
