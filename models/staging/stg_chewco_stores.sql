with source as (
    select * from {{source('chewco', 'stores')}}
), 

renamed as ( 
    select 
        stores_id, 
        stores_name, 
        store_city, 
        store_location

    from source 
)

select * from renamed
