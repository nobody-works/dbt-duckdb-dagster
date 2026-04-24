with source as (
    select * from {{ ref('raw__2023_week01__transactions') }}
),

transformed as (
    select
        "Transaction Code",
        regexp_extract("Transaction Code", '^([A-Za-z]+)', 1) as bank,
        case "Online or In-person"
            when 1 then 'Online'
            when 2 then 'In-Person'
        end                                       as transaction_type,
        dayname(strptime("Transaction Date", '%d/%m/%Y %H:%M:%S')) as day_of_week,
        "Customer Code"                           as customer_code,
        cast("Value" as double)                   as value
    from source
)

select * from transformed
