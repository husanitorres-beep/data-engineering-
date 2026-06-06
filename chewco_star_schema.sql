-- models gum company sales tracks products, stores and employees --
create table products(
    products_id serial primary key,
    products_name varchar(100),
    flavor_name varchar(100),
    products_cost numeric
);

create table stores(
    stores_id serial primary key,
    stores_name varchar(100),
    store_city varchar(100),
    store_location varchar(100)
    
);

create table employee(
    employee_id serial primary key,
    employee_name varchar(100),
    employee_role varchar(100)
);

create table sales(
    sales_id serial primary key,
    quantity_sold numeric,
    total_price numeric,
    sales_date date,
    products_id integer references products(products_id),
    stores_id integer references stores(stores_id),
    employee_id integer references employee(employee_id)
);


select table_name 
from information_schema.tables 
where table_schema = 'public';
 
-- had another table which conflicted with this table and had to DROP --
drop table if exists salary_estimado;
drop table if exists employee_job_title;
drop table if exists employee_department;
drop table if exists employee_info;
drop table if exists sales;
drop table if exists employee;
drop table if exists stores;
drop table if exists products;
