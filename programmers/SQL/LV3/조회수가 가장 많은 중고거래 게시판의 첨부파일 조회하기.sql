--문제 : USED_GOODS_BOARD와 USED_GOODS_FILE 테이블에서 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회하는 SQL문을 작성해주세요. 첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬해주세요. 기본적인 파일경로는 /home/grep/src/ 이며, 게시글 ID를 기준으로 디렉토리가 구분되고, 파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성되도록 출력해주세요. 조회수가 가장 높은 게시물은 하나만 존재합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/164671

--정답 쿼리(서브쿼리 사용) : 
SELECT concat('/home/grep/src/' ,f.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD b join USED_GOODS_FILE f on b.BOARD_ID = f.BOARD_ID
where b.views = (
select max(views)
from USED_GOODS_BOARD
)
order by f.file_id desc

--문제에서 조회수가 가장 높은 게시물은 하나만 존재한다고 적혀있기 떄문에 중복값이 없다고 생각하고 max(views)써도 정답
