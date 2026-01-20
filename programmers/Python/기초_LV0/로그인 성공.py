# 문제 : 머쓱이는 프로그래머스에 로그인하려고 합니다. 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.

# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.

# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120883

# 일단 내 풀이는

def solution(id_pw, db):
    answer = ''
    for i in range(len(db)):
        if id_pw[0] in db[i][0]:
            if id_pw[1] in db[i][1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'

# 이렇게 풀었다 조금 비효율적인 코드 일지 모르지만 테스트 케이스는 통과하고 제출 했더니
# 정답률 75% 였다.

def solution(id_pw, db):
    for user in db:
        if id_pw[0] == user[0]:
            if id_pw[1] == user[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'

# 깔끔한 정답은 이것인데 결정적인 차이는 '='과 'in'의 차이이다. 
# in을 쓰면 부분 문자열만 있어도 true로 결과가 리턴되고
# =은 아예 똑같아야 True로 리턴된다.
