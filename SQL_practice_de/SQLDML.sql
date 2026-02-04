select * from persons
--DDl-Data definition language
create table persons(
	id int not null,
	person_name varchar(20) not null,
	birth_date date,
	phone varchar(15) not null,
	constraint pk_persons primary key (id)
)

--add an new column called email to thee persons table
alter table persons 
add email varchar(50) not null

--drop a column phone from persons table
alter table persons
drop column phone
--delete table 
drop table persons

--DML-Data manipulation language
select * from customers
--inserting records into table
insert into customers (id,first_name,country,score)
values
	(6,'Anna','USA',NULL),
	(7,'Sam',NULL,100)

insert into customers (id,first_name,country,score)
values
	(8,'USA','Max',NULL)
insert into customers (id,first_name,country,score)
values
	(9,'Andreas','Germany',NULL)
insert into customers (id,first_name)
values
	(10,'Sahra')

--copying the data from one table to other
insert into persons (id,person_name,birth_date,phone)
select
id,
first_name,
NULL,
'Unknown'
from customers

select * from customers
select * from persons
--updating the value of score where id is 6
update customers
set score =0
where id=6
--updating the score of customer with id 10 to 0
--and update country to 'uk'
update customers
set score = 0,
	country = 'UK'
where id=10
--update all customers with a null score by setting their score to 0
update customers
set score = 0
where score is null
--delete all customers with an id greater than 5
delete from customers
where id>5
--delete all data from table persons
truncate table persons
--retrieve all customers who are not from germany
select * 
from customers
where country<>'germany'
--greater than 500
select *
from customers
where score > 500
--logical operators.
select *
from customers
where country='USA' AND score > 500
--or operator
select *
from customers
where country='USA' or score > 500
--not less than 500

select *
from customers
where not score < 500
--customers between 100 and 500
select *
from customers
where score between 100 and 500

--retieve all customers from either germany or usa
select *
from customers
where country IN ('Germany','USA')
--other than germany and usa
select *
from customers
where country Not IN ('Germany','USA')
--first name start with m
select *
from customers
where first_name like 'M%'
--first name ends with n
select *
from customers
where first_name like '%n'
--first name contains r
select *
from customers
where first_name like '%r%'
--r in third position
select *
from customers
where first_name like '__r%'



