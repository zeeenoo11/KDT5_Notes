# <오전 수업> 
# 복습:
# 1) set foriegn_key_checks=0 쓰는 이유: 
# 	- person_id는 다른 테이블과 연결돼 있으므로
# 2) ; 은 명령의 끝이라는 뜻

# 3) insert, select, where 3대장
# 4) where 조건 : '=' 한개임
# 5) delete from 테이블명 (where)
#		- where 없으면 테이블 내용 전체
# 6) update 테이블 set (조건)필드1=값1, 필드2=값2, ...
# 	 where 필드=데이터;
#	 => where 조건인 데이터에서 set 조건만 변경

# <Ch.3 쿼리 입문> =================================

# 0.쿼리절: sql은 select, from 등 여러 절로 구성
# 		- 6가지의 절을 볼 예정

# [ 1. select절 ]---------------------------------
# 시작하기
use sakila;
select * from `language` ; # 6개의 언어와 모든 칼럼 출력

# 일부 열만 검색
select language_id, name, last_update from `language` ;
select name from `language` l ; # 이름만 출력

# 추가하기: 숫자 또는 문자열, 표현식, 함수 호출
# 열의 별칭 추가하기: 
select language_id,
	'COMMON' language_usage,
	language_id * 3.14 lang_pi_value,
	upper (name) language_name
from `language` l ;
	
# 위 문장은 AS 를 생략한 것
# - 나중에도 뜬금없이 이름이 나온다 = AS 생략된 것
select language_id,
	'COMMON' as language_usage,
	language_id * 3.14 as lang_pi_value,
	upper (name) as language_name
from `language` l ;

# 중복 제거
select actor_id from film_actor fa order by actor_id ;
# - 1 1 1 1 => 중복된 id 발생
# - all 키워드: 기본값, 명시적으로 지정할 필요 없음 (언제 쓰이는거야)

# [ distinct ] 
# - select 뒤에 distinct
# - 중복을 제거함
select distinct actor_id from film_actor fa order by actor_id;

# [ 2. from 절 ]---------------------------------
# 1) 쿼리에 사용되는 테이블 명시
# 2) 테이블 연결 수단

# 테이블 유형:
# 1. 영구 테이블
# 	- create table로 생성
# 	- 실제 데이터베이스에 존재하는 테이블
# 2. 파생 테이블
# 	- 하위 쿼리에서 반환하고 메모리에 보관된 행
# 3. 임시 테이블
# 4. 가상 테이블

# [ 파생 테이블 ] from절로 생성된다
# - from절 내 select는 파생테이블을 생성한다

# - cust. : 아래 from절에서 as로 축약 선언됨 (customer)
select concat(cust.last_name, ', ', cust.first_name) full_name
from
	(select first_name, last_name, email
	from customer c
	where first_name = 'JESSIE'
	) as cust;

# [ 임시 테이블 ] 휘발성; 데이터베이스 세션이 닫힐 때 사라짐
# : temporary table 이라 표현

# 1. 임시테이블 생성
create temporary table actors_j
	(actor_id smallint(5),	# 화면 출력시 5자리 맞춤
	first_name varchar(45),
	last_name varchar(45));
desc actors_j;  # .info()와 유사하네
# 2. 조건에 맞는 데이터만 테이블에 입력
# (조건) where last_name like 'J%'
# 	   : last_name에서 J로 시작하는 데이터
insert into actors_j
	select actor_id, first_name, last_name
	from actor where last_name like 'J%';

select * from actors_j;

# [ 가상 테이블 (view) ]
# view를 통해 데이터를 관리
# view: 시점, 관점 같은 느낌; Views창에서 확인 가능 (확인 완료)

create view cust_vw as
	select customer_id, first_name, last_name, active
	from customer; # view 생성
	
select * from cust_vw; # 확인

select first_name, last_name from cust_vw cv
where active=0; # 가상테이블에서 쿼리 수행 가능

delete view cust_vw; # 뷰 삭제


# (팁)dbeaver 자체에서 sql 명령어를 쓸 수 있다 ----------
# : 데이터베이스 > 테이블 > (우클릭) sql 생성
# - sql 문장으로 뽑아낸다


# [ 3. Where절 ]--------------------------------

# [ join ] [ on ] : 테이블 연결 join (inner join)
# : 두 개 이상의 테이블을 묶어 하나의 결과 집합을 생성
# join: 연결할 테이블 정의
# on  : 연결 조건 제시
# date( ) : 날짜만 반환하는 내장함수
# time( ) : 시간만 반환하는 내장함수
select customer.first_name, customer.last_name,
	time(rental.rental_date) as rental_time
from customer inner join rental
	on customer.customer_id  = rental.customer_id 
where date(rental.rental_date) = '2005-06-14';
# => customer와 rental의 id를 기준으로 묶은 테이블에서
# 	 2015-06-14인 데이터의 이름과 시간을 출력

# 자동완성 시 생기는 알파벳: 축약문!
select c.first_name, c.last_name,
	time(r.rental_date) rental_date
from customer as c inner join rental as r
	on c.customer_id = r.customer_id 
where date(r.rental_date) = '2005-06-14';

# where절
# : and, or, not 연산자 사용
select title, rating, rental_duration 
from film
where (rating ='G' and rental_duration >= 7)
	or (rating ='PG-13' and rental_duration <4)
order by rating;


# [ 4. Group by, having 절 ]----------------------
# [ Group by ] : 열의 데이터를 그룹화
# - 같은 그룹은 묶어줌 -> count

# [ having ] : 그룹화 이후 수행되는 조건 설정
# : where: 그룹화 이전 조건 설정
# having count(*) >= 40 : 우수 고객 찾기

select c.first_name, c.last_name, count(*)
from customer as c inner join rental as r
	on c.customer_id = r.customer_id
group by c.first_name, c.last_name 
having count(*) >= 40;

# [ 5. Order by 절 ]------------------------------
# 지정된 열을 기준으로 결과 정렬
# - 다중 컬럼: 왼쪽부터 정렬
# - 순서: ASC, DESC

# last_name 기준 정렬
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c 
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by c.last_name, c.first_name asc;

# 내림차순 정렬
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c 
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by time(r.rental_date) desc;

# 칼럼 인덱스로 내림차순 정렬 (첫 열이 1)
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c 
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by 1 desc;

# [실습] =====================================

# 3-3. 
select customer_id
from rental
where 

# 3-4.
# - 1) from, on : customer 테이블과 rental 테이블을 join해야 
# 	   			  고객 정보와 대여기록을 연계할 수 있음
# - 2) where	: 조건 설정
# - 3) order by : 정렬 기준, 내림차순
# - 4) select   : 출력할 열을 선택

select c.store_id, c.email, r.rental_date, r.return_date
from customer as c 
	inner join rental as r
	on c.customer_id  = r.customer_id  
where date(r.rental_date) = '2005-06-14'
order by r.return_date desc;


# <오후 수업> 
# ============= < Ch.4 필터링 > =================
# [조건 평가: where절]
# 1) and
where first_name = 'STEVE' and create_date > '2006-01-01';

# 2) or
where first_name = 'STEVE' or create_date > '2006-01-01';

# 3) (괄호) 
where (first_name = 'STEVE' and create_date > '2006-01-01')
and last_name = 'YOUNG';

# 4) not
where not (first_name <> 'STEVE' and last_name <> 'YOUNG');

# 4-2) <>
where first_name <> 'STEVE' and last_name <> 'YOUNG';


# [ 조건 유형 ]------------------------------------
# 

# [date()] 정확한 날짜 추출
select customer_id, rental_date
from rental r 
where date(r.rental_date) <= '2005-06-16'
	and date(r.rental_date) >= '2005-06-14';

# [ between min and max ]
# between 범위 하한값 and 범위 상한값
# - 반드시 하한값 - 상한값 순으로 적는다
select customer_id, rental_date
from rental r 
where date(r.rental_date) between '2005-06-14'
	and '2005-06-14';


# 문자열 범위
select last_name, first_name
from customer c
where last_name between 'FA' and 'FRB';


# [ or 또는 in ] 유한한 값의 집합으로 제한 ----------------

# [ in() ] : 특정 값에 해당되는 조건을 만들 때 사용
select title, rating
from film f 
where rating in ('G', 'PG');

# 서브쿼리와 in : in()에 서브쿼리가 올 수 있음
select title, rating
from film
where rating in (select rating from film where title like '%PET%');
# (= 서브쿼리의 rating을 가진 모든 데이터)

# 조건부분: PET 가 포함된 데이터
select title, rating from film where title like '%PET%';
# where로 쓰기
where rating in ('G', 'PG');
# [not in] 사용
where rating not in ('PG-13', 'R', 'NC-17')


# [ 문자열 부분 가져오기: left, mid, right ] ------------
# left(문자열, n): 가장 왼쪽부터 n개
select left('abcdefg', 3)
# mid(문자열, 시작 위치, n)
# 	- substr( ) 도 동일한 기능
select mid('abcdefg', 2, 3)

# 


# [와일드카드] like 연산자 사용
# '_' : 정확히 한 문자 ( _A : A앞 한 글자가 있는 것을 찾음)
# '%' : 개수 노상관
# like 연산자를 사용
select last_name, first_name
from customer c 
where last_name like '_A_T%S';

# ^   : 시작
# [ ] : 범위
# regexp : 정규표현식, 정규식
# ^[QY] : Q 또는 Y로 시작하는 단어 검색
select last_name, first_name
from customer
where last_name REGEXP '^[QY]';

# [ Null ] ---------------------------------
# null: 해당 사항 없거나 정의되지 않은 값

# [ is null ]
where return_date is null;

# [ is not null ]
where return_date is not null;

# [null과 조건 조합]
# 미반납 혹은 2005년 5월 ~ 8월 사이가 아닌 경우
# is null / not between
where return_date is null
or return_date not between '2005-05-01' and '2009-09-01';
# 복습) between은 시작 <= 날짜 < 종료


# 실습 패스
# [복습]
# 오늘 한 내용
# 오전 1) 
# 오후 1) 조건 평가, 



