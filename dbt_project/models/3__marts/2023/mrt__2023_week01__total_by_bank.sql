select
    bank,
    sum(value) as total_value
from {{ ref('stg__2023_week01__transactions') }}
group by bank
order by bank
