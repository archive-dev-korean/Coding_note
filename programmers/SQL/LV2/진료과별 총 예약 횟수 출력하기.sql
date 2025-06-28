--문제 : APPOINTMENT 테이블에서 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회하는 SQL문을 작성해주세요. 이때, 컬럼명은 '진료과 코드', '5월예약건수'로 지정해주시고 결과는 진료과별 예약한 환자 수를 기준으로 오름차순 정렬하고, 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/132202

SELECT MCDP_CD as 진료과코드, count(*) as 5월예약건수
from APPOINTMENT 
# where APNT_YMD between '2022-05-01' and '2022-05-31'
where APNT_YMD like '2022-05%'
group by MCDP_CD
order by 2 asc, 1 asc

--조건을 다른 형식으로 줘서 정잡을 구할 수 있음 betwwen과 like로 
