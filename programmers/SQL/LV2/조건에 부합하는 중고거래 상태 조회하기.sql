--문제 : USED_GOODS_BOARD 테이블에서 2022년 10월 5일에 등록된 중고거래 게시물의 게시글 ID, 작성자 ID, 게시글 제목, 가격, 거래상태를 조회하는 SQL문을 작성해주세요. 거래상태가 SALE 이면 판매중, RESERVED이면 예약중, DONE이면 거래완료 분류하여 출력해주시고, 결과는 게시글 ID를 기준으로 내림차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/164672

SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, 
case 
    when status = 'DONE' then '거래완료'
    when status = 'SALE' then '판매중'
    when status = 'RESERVED' then '예약중'
    else status
end as status
from USED_GOODS_BOARD 
where CREATED_DATE = '2022-10-05'

order by 1 desc

--상태에 따라 내용을 다르게 정의해야 해서 case문 사용
