with source as (
    select * from {{ source ('ecom',  'raw_customers') }}
),

renamed as (
    select 
    "ID" as customer_id, "NAME" as customer_name
    from source 

)

select * from renamed


