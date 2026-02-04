use MyDatabase
select * from customers
--show list of customers first name together with their country
select concat(first_name,' ',country)
from customers
--upper and lower functions
select upper(first_name)
from customers
select lower(first_name)
from customers
--trim
--find customers first name leading and trailing spaces
select
	first_name
from customers
where first_name!=TRIM(first_name)
--len function
select
	first_name,
	len(first_name) as len_name
from customers
--trim leading and trailing spaces for first name
select
	first_name,
	len(first_name) as len_name,
	len(trim(first_name)) as len_trim_name
from customers
--replace function
--remove dashes from phone number
select
'123-4567-789' as phone,
replace('123-4567-789','-','/') as clean_phone
select
'report.txt' as phone,
replace('report.txt','.txt','.csv') as clean_phone
--len of first name
select 
	first_name,
	len(first_name) as len_first_name
from customers
--string left and right
select 
	first_name,
	left(trim(first_name),2) as two_chars
from customers
select 
	first_name,
	right(first_name,2) as two_chars
from customers
--substring
select 
	first_name,
	SUBSTRING(first_name,2,len(first_name)) as substr_of_first_name
from customers

--number functions
--round
select 3.516,
round(3.516,2) as round_2,
round(3.516,1) as round_1,
round(3.516,0) as round_0
--abs
select 
	-10,
	abs(-10),
	abs(10)
--date and time functions
use salesdb
--getdate()
select
	OrderId,
	CreationTime,
	'2025-08-20'  hardCoded,
	getdate() Today
from dbo.orders

--extraction parts of the date
select
	day('2025-08-20') as day
select
	month('2025-08-20') as month
select
	year('2025-08-20') as year
select
	OrderId,
	CreationTime,
	datepart(year,CreationTime) year_dp,
	datepart(hour,CreationTime) hour_dp,
	datepart(MINUTE,CreationTime) minute_dp,
	datepart(quarter,CreationTime) quarter_dp,
	datepart(week,CreationTime) week_dp,
	--datename
	datename(month,CreationTime) month_dn,
	datename(day,CreationTime) day_dn,
	datename(weekday,CreationTime) wewk_dn,
	--datetrunc()
	datetrunc(minute,CreationTime) minute_dt,
	datetrunc(day,CreationTime) day_dt,
	datetrunc(year,CreationTime) year_dt,
	year(CreationTime) year_,
	month(CreationTime) month_,
	day(CreationTime) day_
from dbo.orders
--month wise count of orders
select
	datetrunc(month,CreationTime) creation,
	count(*)
from dbo.orders
group by datetrunc(month,CreationTime)
--year wise count of orders
select
	datetrunc(year,CreationTime) creation,
	count(*)
from dbo.orders
group by datetrunc(year,CreationTime)
--eomonth()
select
	OrderId,
	CreationTime,
	EOMONTH(CreationTime) EndOfMonth,
	cast(datetrunc(month,CreationTime)as date) Start_of_month
from dbo.orders
--how many orders were placed each year
select 
	datepart(year,creationtime),
	count(*)
from dbo.orders
group by datepart(year,creationtime)
--how many orders were placed each month
select 
	datepart(month,creationtime),
	count(*)
from dbo.orders
where month(orderdate)=2
group by datepart(month,creationtime)
--formatting
select 
	orderid,
	creationtime,
	format(creationtime,'MM-dd-yyyy') USA_Format,
	format(creationtime,'dd') dd,
	format(creationtime,'ddd') ddd,
	format(creationtime,'dddd') dddd,
	format(creationtime,'MM') MM,
	format(creationtime,'MMM') MMM,
	format(creationtime,'MMMM') MMMM
from dbo.orders
--show creation time in following format
--day wed jan Q1 2025 12:34:56 PM
select
	orderid,
	creationtime,
	'DAY '+Format(creationtime,'ddd MMM')+' Q'+Datename(quarter,creationtime)+' '+format(CreationTime,'yyyy hh:mm:ss tt') as customformat
from dbo.orders
--convert()
select
	'123',
	convert(int,'123') as [string to int convert],
	convert(date,'2025-08-20') as [string to date convert],
	convert(date,CreationTime) as [string to date convert]
from dbo.orders

select
	convert(date,CreationTime) as [string to date convert],
	convert(varchar, creationtime,32) AS [usa std. style:32],
	convert(varchar, creationtime,1) AS [usa std. style:1]
from dbo.orders
--cast
select
	cast('123' as int) as [string to int],
	creationtime,
	cast(creationtime as date) as [datetime to date]
from dbo.orders
--dateadd()
select
	OrderId,
	OrderDate,
	Dateadd(year,2,OrderDate) as TwoYearsLater,
	Dateadd(month,3,OrderDate) as threeMonthsLater,
	Dateadd(day,-10,OrderDate) as TenDaysBefore
from dbo.orders
--calculate the age of employees
select
	employeeid,
	birthdate,
	Datediff(year,birthdate,getdate()) Age
from dbo.employees
--find the average shipping duration in each month
select
	orderid,
	orderdate,
	shipdate,
	datediff(day,orderdate,shipdate) as shipping_duration
from dbo.orders
--find the average shipping duration in days for each month
select
month(orderdate) as orderdate,
avg(datediff(day,orderdate,shipdate)) as avgship
from dbo.orders
group by month(orderdate)
--find the number of days in each order and previous order
select
	orderid,
	orderdate currentorderdate,
	lag(orderdate) over (order by orderdate) prevorderdate,
	datediff(day,lag(orderdate) over (order by orderdate), orderdate) [no.of days]
from dbo.orders
--isdate()
select
	isdate('123') datecheck,
	isdate('2025-08-20') datecheck,
	isdate('20-08-2025') datecheck,
	isdate('2025') datecheck
--cast (orderdate as date)
select
	orderdate,
	isdate(orderdate),
	case when isdate(orderdate)=1 then cast(orderdate as date)
	else '9999-01-01'
	end newOrderDate
from
(
	select '2025-08-20' as orderdate union
	select '2025-08-21' union
	select '2025-08-23' union
	select '2025-08'
)t
--find the average scores for customers
select
	customerid,
	score,
	avg(score) over() avgscore,
	avg(coalesce(score,0)) over() avgscore2
from dbo.customers

--display the full name of customers in a single field
--by merging their firstname and lastnames,
--and add 10 bonus points to each customers score
select
	customerid,
	firstname,
	lastname,
	coalesce(lastname,' ') lastname2,
	firstname+' '+coalesce(lastname,'') as fullname,
	score,
	coalesce(score,0)+10 as scorewithbonus
from dbo.customers
--sort the customers from lowest to highest scores
--with nulls appearing last
select
	customerid,
	score
from dbo.customers
order by case when score is null then 1 else 0 end, score
--find sales price  for each order by dividing sales by quantity
select
	orderid,
	sales,
	quantity,
	sales/nullif(quantity,0) as quant
from dbo.orders
--identify customers who has no scores
select
	*
from dbo.customers
where score is null
--identify customers who has  scores
select
	*
from dbo.customers
where score is not null
--list of all details of customers who have not placed any orders
select 
c.*
from customers as c
left join orders as o
on c.customerid=o.customerid
where o.orderid is null

with orders as (
select 1 id,'A' category union
select 2, null union
select 3, '' union
select 4,'  '
)
select *,
datalength(category) categoryLen,
datalength(trim(category)) policy1,
nullif(trim(category),'') policy2
from orders
--generate a report showing the total sales for each category
select
category,
sum(sales) as totalsales
from(
	select
	orderid,
	sales,
	case
		when sales>50 then 'High'
		when sales>20 then 'medium'
		else 'low'
	end category
	from dbo.orders
)t
group by category
order by totalsales desc
--retrive employees wit gender displayed as full text
select
	employeeid,
	firstname,
	lastname,
	gender,
	case
		when gender='F' then 'Female'
		when gender='M' then 'Male'
		else 'Not available'
	end genderFullText
from dbo.employees
--retrive customers details wit abbrevated country code
use salesdb
select
	customerid,
	firstname,
	lastname,
	country,
	case
		when country='Germany' then 'DE'
		when country='USA' then 'US'
		else 'n/a'
	end countryabbr
from dbo.customers
--find the average score of customers and treat nulls as 0
--and additional provide details such as customerid & lastname
select 
	customerid,
	lastname, 
	avg(
	case 
		when score is null then 0
		else score
		end) over() averagescore

from dbo.customers

--count how many times each customer has made an order with sales greater than 30
select 
	customerid,
	sum(case
		when sales>30 then 1
		else 0
	end) totslOrdersHighSales,
	count(*) TotalOrders
from dbo.orders
group by customerid
order by totslOrdersHighSales desc

