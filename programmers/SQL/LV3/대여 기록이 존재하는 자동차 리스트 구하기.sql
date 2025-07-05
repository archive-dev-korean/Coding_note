--문제 : CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력하는 SQL문을 작성해주세요. 자동차 ID 리스트는 중복이 없어야 하며, 자동차 ID를 기준으로 내림차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/157341

--정답1(where 조건절 사용) : 
SELECT distinct c.CAR_ID
from CAR_RENTAL_COMPANY_CAR c join CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.CAR_ID = h.CAR_ID
where c.CAR_TYPE ='세단' and h.START_DATE like '2022-10%'
order by 1 desc

--정답 2(jojn 조건에 조건주고 한꺼번에 조인) : 
SELECT DISTINCT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS C 
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
    ON C.CAR_ID = H.CAR_ID
    AND C.CAR_TYPE = '세단'
    AND MONTH(H.START_DATE) = 10
ORDER BY C.CAR_ID DESC  

--성능 면, 가독성 면에서는 첫번쨰 적은 정답이 가장 권장 되지만 join절에 조건을 줘서 조인 하는 것은 데이터 양이 방대할 경우 성능 향상이 조금 더 있을 수 있음. 하지만 꼭 그런건 아니고 비교해 봐야함.
