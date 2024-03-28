use shoppingmall;

# 1)
select userName, prodName, addr,
concat(
	mobile1, mobile2
	) as 연락처
from user_table as ut
	inner join buy_table as bt
	on bt.userID = ut.userID ;

# 2)
select ut.userID, userName, prodName, addr,
concat(
	mobile1, mobile2
	) as 연락처
from user_table as ut
	inner join buy_table as bt
	on bt.userID = ut.userID 
where ut.userID = 'KYM';

# 3)
select ut.userID, userName, prodName, addr,
concat(
	mobile1, mobile2
	) as 연락처
from user_table as ut
	inner join buy_table as bt
	on bt.userID = ut.userID 
order by ut.userID ;

# 4)
select distinct ut.userID, userName, addr,
concat(
	mobile1, mobile2
	) as 연락처
from user_table as ut
	inner join buy_table as bt
	on bt.userID = ut.userID 
order by userID ;

# 5)
select ut.userID, userName, addr
from user_table as ut
	inner join buy_table as bt
	on bt.userID = ut.userID 
where addr in ('경북', '경남')
order by userID ;