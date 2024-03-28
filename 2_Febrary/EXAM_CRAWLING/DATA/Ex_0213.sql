create database scraping;

use scraping; # 새 데이터 베이스 생성

create table pages (
    id BIGINT not null auto_increment,
    title VARCHAR(200),
    content VARCHAR(10000),
    created TIMESTAMP default CURRENT_TIMESTAMP, # 현재 시간 자동 입력
    primary key(id)
);

desc pages;
# Test1
insert into pages(title, content)
value(
    "Test page title",
     "This is some test page content. It can be up to 10,000 characters long.");

select * from pages;
# Test2
insert into pages(title, content)
values(
       "Second page title",
       "This is the second test page content"
      );


