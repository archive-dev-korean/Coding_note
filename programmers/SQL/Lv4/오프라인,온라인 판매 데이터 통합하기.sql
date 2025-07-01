--문제 : ONLINE_SALE 테이블과 OFFLINE_SALE 테이블에서 2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품ID, 유저ID, 판매량을 출력하는 SQL문을 작성해주세요. OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시해주세요. 결과는 판매일을 기준으로 오름차순 정렬해주시고 판매일이 같다면 상품 ID를 기준으로 오름차순, 상품ID까지 같다면 유저 ID를 기준으로 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131537

--오답 : 
# SELECT date_format(ons.SALES_DATE, '%Y-%m-%d') as SALES_DATE, ons.PRODUCT_ID, ons.USER_ID, ons.SALES_AMOUNT
# from ONLINE_SALE ons left outer join OFFLINE_SALE ofs
# on ons.PRODUCT_ID = ofs.PRODUCT_ID
# where ons.SALES_DATE like '2022-03%' 
# # and ifnull(ons.USER_ID, "NULL")
# group by 2
# order by 1, 2, 3

--너무나 당연히 join을 사용함. 문제는 offline_sale에는 user_id 컬럼이 없다는 것, 또한 이너 조인이라서 null값은 자동적으로 제외됨
--outer join으로 하려고 해도 중복되는 컬럼 값이 마땅치 않음 
--결국 union 사용해야함

--정답 : 
select DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'
UNION all
SELECT date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT 
FROM OFFLINE_SALE
where SALES_DATE like '2022-03%'
order by sales_date, product_id, user_id

--이렇게 적으면 데이터 증폭 + 원하는 조건 줘서 결과 값 출력.
