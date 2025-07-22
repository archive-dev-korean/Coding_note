-- 문제 : 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요.
-- 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬해주세요.

-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/144856

SELECT a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(b.PRICE * s.SALES) as TOTAL_SALES
from BOOK_SALES s join BOOK b on s.BOOK_ID = b.BOOK_ID join AUTHOR a on a.AUTHOR_ID = b.AUTHOR_ID
where s.SALES_DATE like '2022-01%'
group by a.AUTHOR_ID, b.CATEGORY
# having s.SALES_DATE like '2022-01%'
order by 1, 3 desc

-- 가장 깔끔하게 적으면 될 것 같고, 일단 having절에 조건을 주려고 했지만 이러면 조건주기가 어려워서 where절로 뻈다
