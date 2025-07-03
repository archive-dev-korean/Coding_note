# 암기사항
-----
- concat 과 concat_ws 는 다름 concat_ws 는 구분자 기준으로 합칠 때 사용할 수 있음 또한 null 값은 자동으로 생략함 concat_ws 사용할 때 ()에서 맨처음에 구분자 적어줌 ' ' 나 '-' 같이
- concat은 null이 있을 경우 전체가 null 

------
- 윈도우 함수
  - 여러 행에 대한 계산 결과를 각 행에 반환하는 함수
    
    `<집계 함수> OVER (
    [PARTITION BY 컬럼]   -- 그룹 나누기 (선택)
    ORDER BY 컬럼        -- 정렬 기준 (보통 필수)
    [ROWS BETWEEN ...]   -- 범위 지정 (선택)
)`
- NTILE 함수
  - NTILE(N)은 정렬된 데이터를 N등분하여 각 행에 그룹 번호(1~N)를 부여하는 함수 백분위 구간처럼 등분해서 나누고 싶을 떄 자주 사용
  - 문법 :
    - NTILE(N) OVER (ORDER BY 정렬기준)
- 퍼센트 계산 : 값/전체합 * 100 으로 계산
  - 예시: `ROUND(SIZE * 100.0 / SUM(SIZE) OVER (), 1) AS PERCENT`
