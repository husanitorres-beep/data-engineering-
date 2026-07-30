

create table employees (
	id serial primary key,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	salary numeric(10,2),
	country varchar(50)
);



insert into employees ( first_name, last_name , salary, country) 
values('Robert', 'Steven' , 50000 , 'italy'),
('Emilly', 'Watson' , 10000 , 'china'),
('Amy', 'Sillow' , 100000 , 'brazil'),
('kellis', 'kendrick' , 90000 , 'germany'),
('jake', 'Zaruco' , 50000 , 'usa');


SELECT first_name, country, salary
FROM employees
WHERE salary > 70000;

SELECT country, AVG(salary)
FROM employees
GROUP BY country;

-- update --
update employees
set job_title = 'Data engineer'
where first_name = 'Amy'

select * from employees 


select first_name , salary, departmnets, avg(salary), over (partition by department) as avg_dept_salary 
from employees .
group by departmnets, first_name, salary , avg_dept_salary 
having avg(avg_dept_salary) > 50000



