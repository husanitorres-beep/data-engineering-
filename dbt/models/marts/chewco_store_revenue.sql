with sales as (
    select * from {{ref('stg_chewco_sales')}}
), 

store as (
    select * from{{ref('stg_chewco_stores')}}
),

final as (
    select
       stores.stores_name,
       sum(sales.total_price) as total_revenue
    from sales 
    join stores on stores.stores_id = sales.stores_id
    group by stores.stores_name 
)

select * from final 