-- 문제 : PATIENT, DOCTOR 그리고 APPOINTMENT 테이블에서 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성해주세요. 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성해주세요. 결과는 진료예약일시를 기준으로 오름차순 정렬해주세요.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/132204

-- 정답 : 
SELECT a.APNT_NO,p.PT_NAME,p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
from APPOINTMENT a 
join DOCTOR d on a.MDDR_ID=d.DR_ID
join PATIENT p on p.PT_NO=a.PT_NO
where a.APNT_YMD like '2022-04-13%' and a.APNT_CNCL_YN ='N' and a.MCDP_CD ='CS'
order by 6

-- 처음에 여기서도 join 조건을 a.MCDP_CD=d.MCDP_CD 이렇게 줬더니 값이 이사하게 나와서 아닌 것 같아서 위에 처럼 ID 값으로 수정했다.
-- join조건을 조금 더 자세히 살펴보는 주의력이 필요할 것 같다.
