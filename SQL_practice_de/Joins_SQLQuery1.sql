--JOINS
--get all customers along with their orders
--but only for customers who have placed an order
select * from orders
select 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
from customers as c 
join orders as o
on c.id=o.customer_id
--get all customers along with their orders
--including those without orders
select 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
from customers as c
left join orders as o
on c.id=o.customer_id
--get all customers along with their orders, including orders without matching customers
select 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
from customers as c
right join orders as o
on c.id=o.customer_id
--using left join
select 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
from orders as o
left join customers as c
on c.id=o.customer_id
--get all customers and orders
select 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
from orders as o
full join customers as c
on c.id=o.customer_id
--get all customers who haven't place any order
select *
from customers as c
left join orders as o
on c.id=o.customer_id
where o.customer_id is Null

--get all orders without matching customers
select *
from customers as c
right join orders as o
on c.id=o.customer_id
where c.id is Null
--using left join
select *
from orders as o
right join customers as c
on c.id=o.customer_id
where o.customer_id is null
--getting customers without orders and orders without customers
select *
from customers as c
full join orders as o
on c.id=o.customer_id
where c.id is null or
	o.customer_id is null
--get all customers along with their orders 
--but only for customers who have placed an order
select *
from customers as c
left join orders as o
on c.id=o.customer_id
where o.customer_id is not null
--generate all possible combinations of customers and orders
select *
from customers
cross join orders










