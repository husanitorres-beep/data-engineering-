with source as (
    select * from {{source ('chewco', 'products')}}
), 

renamed as (
    select 
        product_id,
        product_name, 
        product_type,
        product_description,
        product_price,
        is_food_item,
        is_drink_item
    from source 
)

select * from renamed 