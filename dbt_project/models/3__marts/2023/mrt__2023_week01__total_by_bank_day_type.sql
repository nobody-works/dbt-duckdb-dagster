select
    bank,
    day_of_week,
    transaction_type,
    sum(value) as total_value
from {{ ref('stg__2023_week01__transactions') }}
group by bank, day_of_week, transaction_type
order by bank, day_of_week, transaction_type
