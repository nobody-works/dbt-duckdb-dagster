select
    bank,
    customer_code,
    sum(value) as total_value
from {{ ref('stg__2023_week01__transactions') }}
group by bank, customer_code
order by bank, customer_code
