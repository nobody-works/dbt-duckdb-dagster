from dagster import ScheduleDefinition, define_asset_job

from .assets import dbt_2019_assets, dbt_2023_assets

dbt_2023_job = define_asset_job(
    name="dbt_2023_job",
    selection=[dbt_2023_assets],
)

dbt_2019_job = define_asset_job(
    name="dbt_2019_job",
    selection=[dbt_2019_assets],
)

daily_2023_schedule = ScheduleDefinition(
    job=dbt_2023_job,
    cron_schedule="5 0 * * *",
    execution_timezone="Asia/Tokyo",
)

daily_2019_schedule = ScheduleDefinition(
    job=dbt_2019_job,
    cron_schedule="15 0 * * *",
    execution_timezone="Asia/Tokyo",
)
