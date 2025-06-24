--문제 : AIR_POLLUTION 테이블에서 수원 지역의 연도 별 평균 미세먼지 오염도와 평균 초미세먼지 오염도를 조회하는 SQL문을 작성해주세요. 이때, 평균 미세먼지 오염도와 평균 초미세먼지 오염도의 컬럼명은 각각 PM10, PM2.5로 해 주시고, 값은 소수 셋째 자리에서 반올림해주세요.
--결과는 연도를 기준으로 오름차순 정렬해주세요.
--출처: https://school.programmers.co.kr/learn/courses/30/lessons/284530

--오답 쿼리:
select year(YM) as YEAR, round(avg(PM_VAL1),2) as PM10, round(avg(PM_VAL2),2) as PM2.5
from AIR_POLLUTION 
where LOCATION2 like '%수원%'
-- group by YEAR(YM)
group by YEAR
order by YEAR asc

-- 일단 PM2.5를 컬럼명으로 쓸 수 없어서 ''또는 `로 감싸줘야함
-- group by에서는 year 사용 불가(별칭 사용 불가)

--정답 쿼리:
select year(YM) as YEAR, round(avg(PM_VAL1),2) as PM10, round(avg(PM_VAL2),2) as `PM2.5`
from AIR_POLLUTION 
where LOCATION2 like '%수원%'
group by YEAR(YM)
order by YEAR asc

--참고사항 : LOCATION like %수원% 을 LOCATION2 in ('수원')이렇게도 표현 가능
