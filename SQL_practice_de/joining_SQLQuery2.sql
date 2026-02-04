use salesdb
--retrive list of all orders, along with their related customer,product,and employee
select * from orders
select * from customers
select * from employees
select * from orders_archive
select * from products
select 
	o.orderid,
	o.sales,
	c.firstname as customerFirstName,
	c.lastname as customerLastName,
	p.product as productname,
	p.price,
	e.firstname as employeeFirstName,
	e.lastname as employeeLastName

	
from orders as o
left join customers as c on c.customerid=o.customerid
left join products as p on p.productid=o.productid
left join employees as e on e.employeeid=o.salespersonid
--combine the data from employees and customers into on table
select 
	firstname,
	lastname
from customers
union 
select 
	firstname,
	lastname
from employees
--combine the data from employees and customers into on table including duplicates
select 
	firstname,
	lastname
from customers
union all
select 
	firstname,
	lastname
from employees
--who are not employees at same time
select 
	firstname,
	lastname
from customers
Except
select 
	firstname,
	lastname
from employees
--find the employees who also customers
select 
	firstname,
	lastname
from customers
intersect
select 
	firstname,
	lastname
from employees




