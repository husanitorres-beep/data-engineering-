with source as (
    select * from {{source ('chewco', 'sales')}}
), 

renamed as (
    select  
        sales_id, 
        quantity_sold as sold_quantity,
        total_price, 
        sales_date, 
        products_id,
        stores_id,
        employee_id
    from source 

)
select * from renamed 
