--문제 : CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 평균 대여 기간이 7일 이상인 자동차들의 자동차 ID와 평균 대여 기간(컬럼명: AVERAGE_DURATION) 리스트를 출력하는 SQL문을 작성해주세요. 평균 대여 기간은 소수점 두번째 자리에서 반올림하고, 결과는 평균 대여 기간을 기준으로 내림차순 정렬해주시고, 평균 대여 기간이 같으면 자동차 ID를 기준으로 내림차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/157342

--오답 쿼리 :
SELECT CAR_ID, round(avg(datediff(END_Date, start_Date)) ,1) as average_duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
# where datediff(END_DATE , START_DATE) >= 7
group by CAR_ID
order by average_duration desc, CAR_ID desc

--여기서 당일부터 날짜를 계산해야 하기 떄문에 datediff에 +1을 해줘야 함 
--그리고 평균 대여 기간이 7일 이상인 자동차만 조회하는 건데 날짜 차이 계산만 실행해서 다른 값이 조회됨

--정답 쿼리:
SELECT CAR_ID, round(avg(datediff(END_Date, start_Date)+1) ,1) as average_duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
group by CAR_ID
having avg(datediff(END_DATE, start_Date) +1) >=7
order by average_duration desc, CAR_ID desc

--평균 대여 기간 구하는게 문제 조건이라서 집계함수 사용가능한 having절에 조건을 주가해서 사용함
