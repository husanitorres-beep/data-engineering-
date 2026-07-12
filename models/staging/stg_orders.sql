with

source as (

    -- {# This references seed (CSV) data - try switching to {{ source('ecom', 'raw_orders') }} #}
    select * from {{ ref('raw_orders') }}

),

renamed as (

    select

        ----------  ids
        "ID" as order_id,
        "STORE_ID" as location_id,
        "CUSTOMER" as customer_id,

        ---------- numerics
        "SUBTOTAL" as subtotal_cents,
        "TAX_PAID" as tax_paid_cents,
        "ORDER_TOTAL" as order_total_cents,
        {{ cents_to_dollars('"SUBTOTAL"') }} as subtotal,
        {{ cents_to_dollars('"TAX_PAID"') }} as tax_paid,
        {{ cents_to_dollars('"ORDER_TOTAL"') }} as order_total,

        ---------- timestamps
        cast("ORDERED_AT" as date) as order_date

    from source

)

select * from renamed
