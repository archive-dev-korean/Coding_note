--문제 : CAR_RENTAL_COMPANY_CAR 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차가 자동차 종류 별로 몇 대인지 출력하는 SQL문을 작성해주세요. 이때 자동차 수에 대한 컬럼명은 CARS로 지정하고, 결과는 자동차 종류를 기준으로 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/151137

--오답 쿼리1 :
SELECT CAR_TYPE, count(CAR_TYPE) as CARS
from CAR_RENTAL_COMPANY_CAR 
# where OPTIONS in ('통풍시트', '열선시트', '가죽시트')
group by car_type
order by 1 asc

--options가 리스트 형식으로 되어 있어서 이렇게 적으면 아예 출력이 안됨
--like 조건으로 조회하거나 정규 표현식으로 조회하는 방법 2가지로 수정
--count(car_type)이 문제는 없어 보이지만 문제가 될 경우 대비해서 count(*)로 수정

--정답 1(다중 like 사용) : 
SELECT CAR_TYPE, count(*) as CARS
from CAR_RENTAL_COMPANY_CAR 
where options like '%통풍시트%' or
options like '%열선시트%' or
options like '%가죽시트%'
group by car_type
order by 1 asc


--정답 2(정규 표현식) : 
SELECT 
    CAR_TYPE, 
    COUNT(*) AS CARS
FROM 
    CAR_RENTAL_COMPANY_CAR
WHERE 
    OPTIONS REGEXP '통풍시트|열선시트|가죽시트'
GROUP BY 
    CAR_TYPE
ORDER BY 
    CAR_TYPE ASC;

-- 정규 표현식에서 '|'은 or 임
