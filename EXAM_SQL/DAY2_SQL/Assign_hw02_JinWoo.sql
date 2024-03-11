use sqlclass_db;  # 데이터베이스 사용

select * from nobel n ;  # nobel 테이블 확인
desc nobel ;  # 데이터 타입 확인

# 1) 1960 노벨 물리학상 또는 평화상을 수상한 사람
select year, category, fullname
from nobel n 
where year = 1960 
and (category = 'Physics' or category = 'Peace');

# 2) About Albert Einstein
select year, category, birth_continent, birth_country
from nobel n 
where fullname ='Albert Einstein';

# 3) 1910~2010 노벨 평화상 수상자 명단 (연도 오름차순)
select year, fullname, birth_country
from nobel n 
where (1910 <= year and year <= 2010) 
and category ='Peace'
order by year;

# 4) 'John'
select category, fullname
from nobel n 
where fullname like 'John%';

# 5) 1964' 화학, 의학상 제외한 수상자의 모든 정보 (이름 오름차)
select * from nobel
where year=1964 and
category <> 'Chemistry' and
category <> 'Physiology or Medicine'
order by fullname;

# 6) 2000~2019 노벨 문학상
select year, fullname, gender, birth_country
from nobel n 
where (2000 <= year and year <=2019) 
and category = 'Literature';

# 7) 각 분야별 역대 수상자의 수, 내림차순 정령
select count(*)
from nobel	
group by category 
order by count(*) desc;

# 8) 노벨 의학상 있었던 연도
select distinct year
from nobel n 
where category = 'Physiology or Medicine';

-- select distinct yr.year
-- from
-- 	(select year
-- 	from nobel n 
-- 	where category = 'Physiology or Medicine'
-- 	) as yr;

# 9) 노벨 의학상 없던 연도의 총 회수
select count(distinct year) as 히히
from nobel n 
where year not in
	(select distinct year
	from nobel n 
	where category = 'Physiology or Medicine')


# 10) 여성 노벨 수상자의 명단
select fullname, category, birth_country
from nobel n 
where gender = 'female';

# 11) 출생 국가별 횟수 출력
select birth_country, count(*)
from nobel n 
group by birth_country ;

# 12)출생 국가 'Korea'
select * from nobel n 
where birth_country like '%Korea%';

# 13) 출신이 유럽, 북미 외
# 공백은 '' (왜 null엔 포함 안되는거지?)
select * from nobel n 
where birth_continent 
not in ('Europe','North America','');

# 14) 출신 국가별 수상 회수 10회 이상인 국가
select birth_country, count(*) as 횟수
from nobel n 
group by birth_country 
having count(*) >= 10
order by count(*) desc;


-- select * from nobel 
-- where birth_country <> ''
-- and (birth_country in
-- 	(
-- 	select birth_country
-- 	from nobel n 
-- 	group by birth_country
-- 	having count(*) >= 10
-- 	))
-- order by birth_country;

# 15) 이름 공백아닌 2회이상 수상자, 이름 오름차순
select fullname, count(*) as 횟수
from nobel n 
group by fullname
having fullname <> ''
and count(*) >=2
order by fullname;