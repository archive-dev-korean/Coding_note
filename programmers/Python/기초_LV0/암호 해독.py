# 문제 : 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

# 처음에 join메서드 써서 해결함
def solution(cipher, code):
    return ''.join([j for i,j in enumerate(cipher) if (i+1) % code == 0])


# 다음 슬라이싱 하면 자동으로 배수배 되기 떄문에 간편하게 풀 수 있음
def solution(cipher, code):
    return cipher[code -1 ::code]

# 둘다 비슷해 보여서 아무거나 써도 될듯
