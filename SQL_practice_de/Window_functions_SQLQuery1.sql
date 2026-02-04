--multi row functions
--aggregate functions
--find the total number of orders
select
count(*)
from dbo.orders
--find the total sales of orders
select
	count(*) as total_nr_orders,
	sum(sales) as totalsales,
	--avg sales
	avg(sales) as avg_sales,
	--highest sales
	max(sales) max_,
	--lowest sales
	min(sales) as min_
from orders
select * from orders
--find the total sales of orders
--additionally provide details such orderid & orderdate
select
	orderid,
	orderdate,
	sum(sales) over() totalsales
from dbo.orders
--find the total sales for each product
--additionally provide details such orderid & orderdate
select
	orderid,
	orderdate,
	sum(sales) over(partition by productid) totalsales
from dbo.orders
--find the total sales for each combination of product snd order status
--additionally provide details such orderid & orderdate
select
	orderid,
	orderdate,
	sum(sales) over(partition by productid,orderstatus) totalsales
from dbo.orders
--rank each order based on their sales from high to low
--additionally provide details such orderid & orderdate
select
	orderid,
	orderdate,
	sales,
	rank() over(order by sales desc) ranking
from dbo.orders

