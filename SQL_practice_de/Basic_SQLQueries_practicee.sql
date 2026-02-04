select * from customers
--getting specific columns from table
select first_name,country from customers
--filtering data by using where clause
select * from customers where score>350

--customer score not equal to 0
select *
from customers
where score != 0;

--Retrive customers from germany
select *
from customers
where country='Germany'

select 
	first_name,
	country
from customers
where country='Germany'
--sorting data by order by
select *
from customers
order by score desc

--based on country
select *
from customers
order by country asc,score desc
--Aggregate sum of country
select 
	country,
	sum(score) as sum
from customers
group by country
--total score and total number customers for each country
select 
	sum(score) as total_score,
	count(id) as total_customers
from customers
group by country

--having score greater than 800
select 
	sum(score) as total_score,
	count(id) as total_customers
from customers
group by country
having sum(score)>800
--avg score for each country
select 
	country,
	avg(score) as averege_score
from customers
where score!=0
group by country
having avg(score)>430
--Distinct values
select distinct country
from customers
--Top 3 values
select top 3 * from customers
--Top 3 customers with highest scores
select Top 3 *
from customers
order by score desc
--bottom 2 customers with lowest score
select Top 2 *
from customers
order by score Asc
--select last 2 recent orders
select Top 2 *
from orders
order by order_date Desc
--multiple queries in same window
select * 
from customers

select *
from orders
