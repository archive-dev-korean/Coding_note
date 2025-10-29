# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    # 1) 날짜를 총 '일'로 변환 (모든 달=28일, 1년=12*28일)
    def to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return y * 12 * 28 + m * 28 + d

    today_days = to_days(today)

    # 2) 약관 종류 → 유효 개월 수 매핑
    term_months = {}
    for t in terms:
        typ, months = t.split()
        term_months[typ] = int(months)

    # 3) 각 개인정보의 만료일 계산 후 오늘과 비교
    answer = []
    for idx, item in enumerate(privacies, start=1):
        date_str, typ = item.split()            # "YYYY.MM.DD T"
        start_days = to_days(date_str)
        expire_days = start_days + term_months[typ] * 28 - 1  # 유효기간 마지막 날

        # 오늘이 만료일을 지난 경우(오늘 > 만료일) 파기 대상
        if today_days > expire_days:
            answer.append(idx)

    return answer
# 아직 이해 못함 나중에 확인
