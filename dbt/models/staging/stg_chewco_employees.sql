with source as (
    select * from{{source ('chewco', 'employee')}}
), 
renamed as(
    select 
        employee_id,
        employee_name, 
        employee_role
    from source 
)

select * from renamed