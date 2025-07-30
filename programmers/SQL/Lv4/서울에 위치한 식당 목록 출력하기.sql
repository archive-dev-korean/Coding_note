-- 문제 : REST_INFO와 REST_REVIEW 테이블에서 서울에 위치한 식당들의 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회하는 SQL문을 작성해주세요. 이때 리뷰 평균점수는 소수점 세 번째 자리에서 반올림 해주시고 결과는 평균점수를 기준으로 내림차순 정렬해주시고, 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬해주세요.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131118

-- 일단 문제 자체는 어렵지 않다. LV2~3 수준 정도

SELECT i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, round(avg(r.REVIEW_SCORE),2) as SCORE
from REST_INFO i join REST_REVIEW r on i.REST_ID = r.REST_ID
where i.ADDRESS like '서울%'
group by i.REST_ID
order by 6 desc, 4 desc

-- 다만 주의할 점은 group by 를 제대로 써야 한다. 안쓰면 결과값 하나만 출력됨
-- 이것만 주의하면 어렵지 않은 문제다.
